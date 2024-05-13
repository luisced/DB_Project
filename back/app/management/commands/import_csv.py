import pandas as pd
from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware
from datetime import datetime
from app.models import AfectedUser, Device, Geolocalization, CyberAttack
from concurrent.futures import ProcessPoolExecutor, as_completed
import multiprocessing
import numpy as np

# Initialize caches
user_cache = {}
device_cache = {}
geo_location_cache = {}

def get_or_create_geolocation(location_data):
    if location_data not in geo_location_cache:
        try:
            city, locality = location_data.split(', ')
        except ValueError:
            locality = location_data
            city = ''
        geo_location = Geolocalization.objects.filter(locality=locality, city=city).first()
        if not geo_location:
            geo_location = Geolocalization.objects.create(locality=locality, city=city)
        geo_location_cache[location_data] = geo_location

    return geo_location_cache[location_data]

def get_or_create_user(username):
    if username not in user_cache:
        user = AfectedUser.objects.filter(username=username).first()
        if not user:
            user = AfectedUser.objects.create(username=username)
        user_cache[username] = user

    return user_cache[username]


def deviceSplit(device_info):
    try:
        web_browser = device_info.split('(')[0].strip()
        os = device_info.split('(')[1].split(')')[0].strip()
        rest = device_info.split(')')[1].strip()
        return web_browser, os, rest
    except IndexError:
        return device_info, None, None

def get_or_create_device(device_info):
    if device_info not in device_cache:
        web_browser, os, rest = deviceSplit(device_info)
        device = Device.objects.filter(web_browser=web_browser, operative_system=os, rest_information=rest).first()
        if not device:
            device = Device.objects.create(web_browser=web_browser, operative_system=os, rest_information=rest)
        device_cache[device_info] = device

    return device_cache[device_info]



def process_chunk(chunk_data):
    from django import db
    db.connections.close_all()
    import django
    django.setup()

    cyber_attacks_to_create = []
    print(f"Processing chunk of {len(chunk_data)} records...")

    try:
        for _, row in chunk_data.iterrows():
            naive_timestamp = datetime.strptime(row['Timestamp'], '%Y-%m-%d %H:%M:%S')
            aware_timestamp = make_aware(naive_timestamp)

            user = get_or_create_user(row['User Information'])
            device = get_or_create_device(row['Device Information'])
            geo_location = get_or_create_geolocation(row['Geo-location Data'])
            cyber_attack = CyberAttack(
                timestamp=aware_timestamp,
                sourceIP=row['Source IP Address'],
                destinationIP=row['Destination IP Address'],
                sourcePort=row['Source Port'],
                destinationPort=row['Destination Port'],
                protocol=row['Protocol'],
                packetLength=row['Packet Length'],
                packetType=row['Packet Type'],
                trafficType=row['Traffic Type'],
                actionTaken=row['Action Taken'],
                severityLevel=row['Severity Level'],
                networkSegment=row['Network Segment'],
                alertsWarnings=row['Alerts/Warnings']=="Alert Triggered",
                attackType=row['Attack Type'],
                idsIpsAlerts=row['IDS/IPS Alerts']=="Alert Data",
                user=user,
                device=device,
                geoLocation=geo_location
            )
            cyber_attacks_to_create.append(cyber_attack)

        CyberAttack.objects.bulk_create(cyber_attacks_to_create, batch_size=500)
    except Exception as e:
        # Log the exception, consider re-raising or handling it as needed
        print(f"Error processing chunk: {e}")
        return 0

    return len(cyber_attacks_to_create)


class Command(BaseCommand):
    help = 'Import CSV data into the database using multiprocessing for efficiency.'

    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str, help='The CSV file path')

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file_path']
        
        if CyberAttack.objects.exists():
            self.stdout.write(self.style.WARNING('Database already populated. Skipping import.'))
            return 
        
        df = pd.read_csv(csv_file_path)

        # Determine the number of processes based on available CPUs
        num_processes = multiprocessing.cpu_count()

        # Split the DataFrame into chunks for processing
        chunks = np.array_split(df, num_processes)

        # Process chunks in parallel
        total_processed = 0
        with ProcessPoolExecutor(max_workers=num_processes) as executor:
            futures = [executor.submit(process_chunk, chunk) for chunk in chunks]
            for future in as_completed(futures):
                result = future.result()
                self.stdout.write(self.style.SUCCESS(f'Processed {result} records.'))
                total_processed += result

        self.stdout.write(self.style.SUCCESS(f'Successfully processed {total_processed} records.'))

