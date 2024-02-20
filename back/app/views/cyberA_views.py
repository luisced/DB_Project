from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..serializers.cyberAttack_serializers import CyberAttackSerializer, AfectedUserSerializer, DeviceSerializer, GeolocalizationSerializer
from ..models.cyber_attack_models import CyberAttack, AfectedUser, Device, Geolocalization

# GET all cyberAttacks

@api_view(['GET'])
def get_cyberAttacks(request):
    cyberAttacks = CyberAttack.objects.all()
    serializer = CyberAttackSerializer(cyberAttacks, many=True)
    return Response(serializer.data)

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
    serializer = AfectedUserSerializer(afectedUsers, many=True)
    return Response(serializer.data)

# GET all devices

@api_view(['GET'])
def get_devices(request):
    devices = Device.objects.all()
    serializer = DeviceSerializer(devices, many=True)
    return Response(serializer.data)

# GET all geolocalizations

@api_view(['GET'])
def get_geolocalizations(request):
    geolocalizations = Geolocalization.objects.all()
    serializer = GeolocalizationSerializer(geolocalizations, many=True)
    return Response(serializer.data)