from django.db import models
from .base import BaseModel

class ExampleModel(BaseModel):
    """
    Example model to demonstrate model structure in this template.
    This shows common field types and relationships you might use.
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    # Example of relationship fields
    created_by = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        related_name='examples'
    )
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Example'
        verbose_name_plural = 'Examples'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Example of a model method"""
        return f"/api/examples/{self.id}/"
