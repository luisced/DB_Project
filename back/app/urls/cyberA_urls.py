from django.urls import path
from ..views import cyberA_views as views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('cyber-attacks/', views.get_cyberAttacks, name='get_cyberAttacks'),
    path('cyber-attacks/<int:pk>/', views.get_cyberAttack, name='get_cyberAttack'),
    path('afected-users/', views.get_afectedUsers, name='get_afectedUsers'),
    path('devices/', views.get_devices, name='get_devices'),
    path('geolocalizations/', views.get_geolocalizations, name='get_geolocalizations'),
    
    path('cyber-attacks/atype-frequency/', views.atypeFrequency, name='atypeFrequency'),
    path('cyber-attacks/severity-over-time/', views.attacks_by_severity, name='severityOverTime'),
    path('cyber-attacks/most-attacked-devices/', views.mostAttackedDevices, name='mostAttackedDevices'),
    path('cyber-attacks/ids-ips-alerts/', views.idsIpsAlerts, name='idsIpsAlerts'),
    path('cyber-attacks/geo-location/', views.geoLocation, name='geoLocation'),
    path('cyber-attacks/attack-action/', views.attackAction, name='attackAction'),
    path('cyber-attacks/protocol-frequency/', views.protocolFrequency, name='protocolFrequency'),
    path('cyber-attacks/alerts-warnings/', views.alertsWarnings, name='alertsWarnings'),
    path('cyber-attacks/unalerted-attacks/', views.unalerted_attacks_by_country, name='unalerted_attacks_by_country'),
    path('cyber-attacks/attack-types/', views.attack_types_by_country, name='attack_types_by_country'),
]

'''
Links:
http://localhost:8000/cyber-attacks/
http://localhost:8000/cyber-attacks/1/
http://localhost:8000/afected-users/
http://localhost:8000/devices/
http://localhost:8000/geolocalizations/
http://localhost:8000/cyber-attacks/atype-frequency/
http://localhost:8000/cyber-attacks/severity-over-time/
http://localhost:8000/cyber-attacks/most-attacked-devices/
http://localhost:8000/cyber-attacks/ids-ips-alerts/
http://localhost:8000/cyber-attacks/geo-location/
http://localhost:8000/cyber-attacks/attack-action/
http://localhost:8000/cyber-attacks/protocol-frequency/
http://localhost:8000/cyber-attacks/alerts-warnings/
http://localhost:8000/cyber-attacks/unalerted-attacks/
http://localhost:8000/cyber-attacks/attack-types/
'''