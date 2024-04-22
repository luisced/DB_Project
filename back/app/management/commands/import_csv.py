import pandas as pd
from django.core.management.base import BaseCommand
from django.db import transaction
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

def get_or_create_user(name_data):
    if name_data not in user_cache:
        user_cache[name_data]=name_data
        query = AfectedUser.objects.filter(username=name_data)
        if query.exists():
            user_cache[name_data] = query.first()
        else:
            user = AfectedUser.objects.create(username=name_data)
        return user
    return user_cache[name_data]

def deviceSplit(device_info):
    #Before ( = web_browser
    #In () = operative_system
    #After ) = rest_information
    
    web_browser = device_info.split(' (')[0]
    os = device_info.split(' (')[1].split(')')[0]
    rest = device_info.split(') ')[1]
    return web_browser, os, rest

def get_or_create_device(device_info):
    if device_info not in device_cache:
        web_browser, os, rest = deviceSplit(device_info)
        device_cache[device_info][web_browser]=web_browser
        device_cache[device_info][os]=os
        device_cache[device_info][rest]=rest
        query = Device.objects.filter(web_browser=web_browser, os=os, rest=rest)
        if query.exists():
            device_cache[device_info] = query.first()
        else:
            device = Device.objects.create(device=device_info, web_browser=web_browser, os=os, rest=rest)
        return device
    return device_cache[device_info]

def get_or_create_geolocation(location_data):
    if location_data not in geo_location_cache:
        query = Geolocalization.objects.filter(location=location_data)
        if query.exists():
            geo_location_cache[location_data] = query.first()
        else:
            locality , city = location_data.split(', ')
            geo_location = Geolocalization.objects.create(location=location_data, locality=locality, city=city)
        geo_location_cache[location_data] = geo_location
    return geo_location_cache[location_data]


def process_chunk(chunk_data):
    import django
    django.setup()

    cyber_attacks_to_create = []

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

    # Bulk insert
    CyberAttack.objects.bulk_create(cyber_attacks_to_create, batch_size=500)

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

