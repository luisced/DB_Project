from django.core.management.base import BaseCommand
import csv
from django.utils.timezone import make_aware
from datetime import datetime
from app.models import AfectedUser, Device, Geolocalization, CyberAttack

class Command(BaseCommand):
    help = 'Import CSV data into the database, filtering unused columns and handling datetime conversion.'

    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str, help='The CSV file path')

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file_path']
        
        with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            try:
                for row in reader:
                    naive_timestamp = datetime.strptime(row['Timestamp'], '%Y-%m-%d %H:%M:%S')
                    aware_timestamp = make_aware(naive_timestamp)
                    user, _ = AfectedUser.objects.get_or_create(username=row['User Information'])
                    device_information = row['Device Information'][:100]
                    device, _ = Device.objects.get_or_create(device_information=device_information)

                    geo_location, _ = Geolocalization.objects.get_or_create(location=row['Geo-location Data'])
                    CyberAttack.objects.create(
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
                    self.stdout.write(self.style.SUCCESS(f"Imported cyber attack from {row['Source IP Address']} to {row['Destination IP Address']}"))

            except django.db.utils.DataError as e:
                print(f"Error importing row {row}: {e}")