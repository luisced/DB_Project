from django.urls import path
from ..views import cyberA_views as views

urlpatterns = [
    path('cyber-attacks/', views.get_cyberAttacks, name='get_cyberAttacks'),
    path('cyber-attacks/<int:pk>/', views.get_cyberAttack, name='get_cyberAttack'),
    path('afected-users/', views.get_afectedUsers, name='get_afectedUsers'),
    path('devices/', views.get_devices, name='get_devices'),
    path('geolocalizations/', views.get_geolocalizations, name='get_geolocalizations'),
]

