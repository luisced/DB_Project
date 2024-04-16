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

def get_or_create_user(username):
    if username not in user_cache:
        queryset = AfectedUser.objects.filter(username=username)
        if queryset.exists():
            user = queryset.first()
        else:
            user = AfectedUser.objects.create(username=username)
        user_cache[username] = user
    return user_cache[username]

def deviceSplit(device_info):
    '''
Mozilla/5.0 (Android 1.0; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0
Mozilla/5.0 (Android 1.0; Mobile; rv:19.0) Gecko/19.0 Firefox/19.0
Mozilla/5.0 (Android 1.0; Mobile; rv:30.0) Gecko/30.0 Firefox/30.0

web_browser = Mozilla/5.0 everything before (
os = Android 1.0 everything between ( )
rest = Gecko/14.0 Firefox/14.0 everything after )
'''
    web_browser = device_info.split('(')[0]
    os = device_info.split('(')[1].split(')')[0]
    rest = device_info.split(')')[1]
    return web_browser, os, rest

def get_or_create_device(device_info):
    if device_info not in device_cache:
        web_browser, os, rest = deviceSplit(device_info)
        device = Device.objects.create(web_browser=web_browser, operative_system=os, rest_information=rest)
        device_cache[device_info] = device
    return device_cache[device_info]

def get_or_create_geolocation(location_data):
    if location_data not in geo_location_cache:
        locality, city = location_data.split(',')
        geo_location = Geolocalization.objects.create(locality=locality, city=city)
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
        device = get_or_create_device(row['Device Information'][:100])
        geo_location = get_or_create_geolocation(row['Geo-location Data'])

        cyber_attack = CyberAttack(
            timestamp=aware_timestamp,
            sourceIP=row['Source IP Address'],
            destinationIP=row['Destination IP Address'],
            sourcePort=int(row['Source Port']),
            destinationPort=int(row['Destination Port']),
            protocol=row['Protocol'],
            packetLength=int(row['Packet Length']),
            packetType=row['Packet Type'],
            trafficType=row['Traffic Type'],
            actionTaken=row['Action Taken'],
            severityLevel=row['Severity Level'],
            networkSegment=row['Network Segment'],
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

