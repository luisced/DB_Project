from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import example_views

# Create a router and register our viewset
router = DefaultRouter()
router.register(r'examples', example_views.ExampleModelViewSet, basename='example')

# The API URLs are determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
]
