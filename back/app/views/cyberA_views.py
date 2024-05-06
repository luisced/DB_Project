from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
import random
from django.db.models import Count, F, Func, Q
from django.db.models.functions import TruncDay
from django.db import models
from ..serializers.cyberAttack_serializers import CyberAttackSerializer, AfectedUserSerializer, DeviceSerializer, GeolocalizationSerializer
from ..models import CyberAttack, AfectedUser, Device, Geolocalization

# GET all cyberAttacks
@api_view(['GET'])
def get_cyberAttacks(request):
    cyberAttacks = CyberAttack.objects.all()
    paginator = PageNumberPagination()
    paginator.page_size = 100
    result_page = paginator.paginate_queryset(cyberAttacks, request)
    serializer = CyberAttackSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

# GET single cyberAttack
@api_view(['GET'])
def get_cyberAttack(request, pk):
    try:
        cyberAttack = CyberAttack.objects.get(pk=pk)
        serializer = CyberAttackSerializer(cyberAttack, many=False)
        return Response(serializer.data)
    except CyberAttack.DoesNotExist:
        return Response({'error': 'CyberAttack not found'}, status=404)

# Frequency of Each Type of Attack
@api_view(['GET'])
def atypeFrequency(request):
    attackTypes = CyberAttack.objects.values('attackType').annotate(count=Count('attackType')).order_by('-count')
    return Response(attackTypes)

# Severity Levels of Attacks Over Time
@api_view(['GET'])
def attacks_by_severity(request):
    # Annotate data grouping by severity and the hour part of the timestamp
    attack_data = CyberAttack.objects.values(
        severity=F('severityLevel'),
        hour=ExtractHour('timestamp')
    ).annotate(
        count=Count('id')
    ).order_by('severity', 'hour')

    # Initialize a dictionary to hold all severity levels
    severity_dict = {}

    # Fill the dictionary with data for each severity level
    for attack in attack_data:
        severity = attack['severity']
        hour = attack['hour']
        count = attack['count']
        if severity not in severity_dict:
            severity_dict[severity] = {'id': severity, 'data': []}
        severity_dict[severity]['data'].append({'x': int(hour), 'y': count})

    # Convert the dictionary to a list as required
    result = list(severity_dict.values())

    return Response(result)


# Extracts only the hour part of the timestamp
class ExtractHour(Func):
    function = 'EXTRACT'
    template = '%(function)s(HOUR from %(expressions)s)'


# Devices Most Attacked
@api_view(['GET'])
def mostAttackedDevices(request):
    # Define common OS keywords for categorization
    os_keywords = {
        "Windows": Q(operative_system__icontains="Windows"),
        "Linux": Q(operative_system__icontains="Linux"),
        "Android": Q(operative_system__icontains="Android"),
        "macOS": Q(operative_system__icontains="macOS"),
        "iOS": Q(operative_system__icontains="iOS")
    }

    # Initialize the treemap structure
    treemap_data = {
        "name": "Devices",
        "color": generate_random_hsl(),
        "children": []
    }

    # Process each operating system category
    for os_name, os_filter in os_keywords.items():
        # Group devices by web browser under each OS category
        browser_groups = Device.objects.filter(os_filter).values(
            'web_browser'
        ).annotate(
            attack_count=Count('cyberattack')  # Assuming CyberAttack model links to Device
        ).order_by('-attack_count')

        # Create child nodes for each web browser under the parent OS node
        browser_children = [
            {
                "name": f"{browser_group['web_browser']}",
                "loc": browser_group['attack_count'],
                "color": generate_random_hsl()
            }
            for browser_group in browser_groups
        ]

        # Add OS parent node only if browser groups exist
        if browser_children:
            treemap_data['children'].append({
                "name": os_name,
                "children": browser_children,
                "color": generate_random_hsl()
            })

    return Response(treemap_data)

# Generate random HSL color


def generate_random_hsl():
    hue = random.randint(0, 360)
    saturation = random.randint(50, 100)
    lightness = random.randint(40, 60)
    return f'hsl({hue}, {saturation}%, {lightness}%)'


# IDS/IPS Alerts Detection
@api_view(['GET'])
def idsIpsAlerts(request):
    idsIps = CyberAttack.objects.values('idsIpsAlerts').annotate(count=Count('idsIpsAlerts')).order_by('-count')
    alerted = {
        "id": "Alerted",
        "label": "Alerted",
        "value": idsIps[0]['count'],
        "color": generate_random_hsl()
        }
    not_alerted = {
        "id": "Not Alerted",
        "label": "Not Alerted",
        "value": idsIps[1]['count'],
        "color": generate_random_hsl()
        }
    lista = [alerted, not_alerted]
    return Response(lista)
    
        

# Geographical Distribution of Attacks
@api_view(['GET'])
def geoLocation(request):
    geoLocations = CyberAttack.objects.values('geoLocation__city').annotate(count=Count('geoLocation')).order_by('-count')
    return Response(geoLocations)

#calendar heatmap
@api_view(['GET'])
def calendar_heatmap(request):
  
    attack_data = CyberAttack.objects.values(
        day=TruncDay('timestamp')
    ).annotate(
        count=Count('id')
    ).order_by('day')

    
    # Initialize a list to hold the result
    result = []
    
    # Fill the list with data for each day
    for attack in attack_data:
        day = attack['day']
        count = attack['count']
        result.append({'day': day.strftime('%Y-%m-%d'), 'value': count})
        
    return Response(result)
  
  

# Correlation Between Attack Type and Action Taken
@api_view(['GET'])
def attackAction(request):
    attackActions = CyberAttack.objects.values('attackType', 'actionTaken').annotate(count=Count('attackType')).order_by('attackType', 'actionTaken')
    return Response(attackActions)

# Protocol Usage Frequency
@api_view(['GET'])
def protocolFrequency(request):
    protocols = CyberAttack.objects.values('protocol').annotate(count=Count('protocol')).order_by('-count')
    return Response(protocols)

# Alerts and Warnings Generated by Attacks
@api_view(['GET'])
def alertsWarnings(request):
    alerts = CyberAttack.objects.values('alertsWarnings').annotate(count=Count('alertsWarnings')).order_by('-count')
    return Response(alerts)

# GET all affectedUsers
@api_view(['GET'])
def get_afectedUsers(request):
    afectedUsers = AfectedUser.objects.all()
    paginator = PageNumberPagination()
    paginator.page_size = 500
    result_page = paginator.paginate_queryset(afectedUsers, request)
    serializer = AfectedUserSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

# GET all devices
@api_view(['GET'])
def get_devices(request):
    devices = Device.objects.all()
    paginator = PageNumberPagination()
    paginator.page_size = 500
    result_page = paginator.paginate_queryset(devices, request)
    serializer = DeviceSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

# GET all geolocalizations
@api_view(['GET'])
def get_geolocalizations(request):
    geolocalizations = Geolocalization.objects.all()
    paginator = PageNumberPagination()
    paginator.page_size = 500
    result_page = paginator.paginate_queryset(geolocalizations, request)
    serializer = GeolocalizationSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def unalerted_attacks_by_country(request):
    # Query to fetch and aggregate unalerted attacks by country
    attacks_data = CyberAttack.objects.filter(
        alertsWarnings=False,
        geoLocation__isnull=False
    ).values(
        country=F('geoLocation__city')  # Corrected to use 'locality'
    ).annotate(
        count=Count('id')
    ).order_by('-count')

    return Response(attacks_data)

@api_view(['GET'])
def attack_types_by_country(request):
    
    attack_types_data = CyberAttack.objects.filter(
        alertsWarnings=False,
        geoLocation__isnull=False
    ).values(
        'geoLocation__city',
        'attackType'
    ).annotate(
        count=Count('id')
    ).order_by('geoLocation__city', '-count')

    result = {}

    for item in attack_types_data:
        country = item['geoLocation__city']
        attack_type = item['attackType']
        if country not in result:
            result[country] = {'country': country}

        if attack_type not in result[country]:
            color_field = f'{attack_type}Color'
            result[country][attack_type] = item['count']
            result[country][color_field] = generate_random_hsl()

    # Convert the result dictionary to a list of dictionaries as required
    result_list = list(result.values())
    return Response(result_list)


'''

'''