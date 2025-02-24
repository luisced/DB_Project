from django.urls import path
from app.views import health_views

urlpatterns = [
    path('health/', health_views.health_check, name='health-check'),
]
