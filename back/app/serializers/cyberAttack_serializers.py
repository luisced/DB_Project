from rest_framework import serializers
from ..models.cyber_attack_models import CyberAttack, AfectedUser, Device, Geolocalization

class CyberAttackSerializer(serializers.ModelSerializer):
    class Meta:
        model = CyberAttack
        fields = '__all__'

class GeolocalizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geolocalization
        fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class AfectedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AfectedUser
        fields = '__all__'


