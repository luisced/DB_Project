import pandas as pd
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.timezone import make_aware
from datetime import datetime
from app.models import AfectedUser, Device, Geolocalization, CyberAttack
from concurrent.futures import ProcessPoolExecutor
import multiprocessing
import numpy as np


def process_chunk(chunk_data):
    import django
    django.setup()

    cyber_attacks_to_create = []

    for _, row in chunk_data.iterrows():
        naive_timestamp = datetime.strptime(
            row['Timestamp'], '%Y-%m-%d %H:%M:%S')
        aware_timestamp = make_aware(naive_timestamp)
        user, _ = AfectedUser.objects.get_or_create(
            username=row['User Information'])
        device, _ = Device.objects.get_or_create(
            device_information=row['Device Information'][:100])
        geo_location, _ = Geolocalization.objects.get_or_create(
            location=row['Geo-location Data'])

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
    with transaction.atomic():
        CyberAttack.objects.bulk_create(
            cyber_attacks_to_create, batch_size=500)

    return len(cyber_attacks_to_create)


class Command(BaseCommand):
    help = 'Import CSV data into the database using multiprocessing for efficiency.'

    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str,
                            help='The CSV file path')

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
            futures = [executor.submit(process_chunk, chunk)
                       for chunk in chunks]
            for future in futures:
                total_processed += future.result()

        self.stdout.write(self.style.SUCCESS(
            f'Successfully processed {total_processed} records.'))
