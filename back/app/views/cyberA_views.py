from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from ..serializers.cyberAttack_serializers import CyberAttackSerializer, AfectedUserSerializer, DeviceSerializer, GeolocalizationSerializer
from ..models.cyber_attack_models import CyberAttack, AfectedUser, Device, Geolocalization


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
    cyberAttack = CyberAttack.objects.get(id=pk)
    serializer = CyberAttackSerializer(cyberAttack, many=False)
    return Response(serializer.data)


# GET all afectedUsers

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
    serializer = GeolocalizationSerializer(geolocalizations, many=True)
    return Response(serializer.data)