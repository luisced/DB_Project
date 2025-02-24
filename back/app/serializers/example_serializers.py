from rest_framework import serializers
from app.models.example_model import ExampleModel
from app.models.user_models import User

class ExampleModelSerializer(serializers.ModelSerializer):
    """
    Example serializer demonstrating common serializer patterns and features
    """
    created_by_username = serializers.CharField(source='created_by.username', read_only=True)
    days_since_creation = serializers.SerializerMethodField()
    
    class Meta:
        model = ExampleModel
        fields = [
            'id',
            'name',
            'description',
            'is_active',
            'quantity',
            'price',
            'last_updated',
            'created_by',
            'created_by_username',
            'created_at',
            'updated_at',
            'days_since_creation'
        ]
        read_only_fields = ['created_at', 'updated_at', 'last_updated']
        
    def get_days_since_creation(self, obj):
        """Example of a SerializerMethodField implementation"""
        from django.utils import timezone
        if obj.created_at:
            delta = timezone.now() - obj.created_at
            return delta.days
        return None
        
    def validate_quantity(self, value):
        """Example of field validation"""
        if value < 0:
            raise serializers.ValidationError("Quantity cannot be negative")
        return value
        
    def validate(self, data):
        """Example of object-level validation"""
        if data.get('price', 0) < 0 and data.get('is_active', True):
            raise serializers.ValidationError(
                "Active items cannot have negative prices"
            )
        return data
