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

def get_or_create_device(device_info):
    
    web_browser, os, rest_info =

def get_or_create_geolocation(location_data):
    if location_data not in geo_location_cache:
        queryset = Geolocalization.objects.filter(location=location_data)
        if queryset.exists():
            geo_location = queryset.first()
        else:
            geo_location = Geolocalization.objects.create(location=location_data)
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
            payloadData=row.get('Payload Data', ''),
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

