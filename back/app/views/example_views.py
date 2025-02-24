from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from app.models.example_model import ExampleModel
from app.serializers.example_serializers import ExampleModelSerializer

class ExampleModelViewSet(viewsets.ModelViewSet):
    """
    Example ViewSet demonstrating common patterns and features.
    Includes CRUD operations and custom actions.
    """
    serializer_class = ExampleModelSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """Example of queryset filtering"""
        queryset = ExampleModel.objects.all()
        
        # Example of query parameter filtering
        is_active = self.request.query_params.get('is_active', None)
        if is_active is not None:
            queryset = queryset.filter(is_active=is_active)
            
        # Example of related field filtering
        created_by = self.request.query_params.get('created_by', None)
        if created_by:
            queryset = queryset.filter(created_by_id=created_by)
            
        return queryset
    
    def perform_create(self, serializer):
        """Example of custom create logic"""
        serializer.save(created_by=self.request.user)
    
    @action(detail=True, methods=['post'])
    def toggle_active(self, request, pk=None):
        """Example of a custom action"""
        example = self.get_object()
        example.is_active = not example.is_active
        example.save()
        
        serializer = self.get_serializer(example)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def stats(self, request):
        """Example of a custom list action"""
        total_count = self.get_queryset().count()
        active_count = self.get_queryset().filter(is_active=True).count()
        
        return Response({
            'total_count': total_count,
            'active_count': active_count,
            'inactive_count': total_count - active_count
        })
