from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    """Serializer for Todo model"""
    
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'due_date', 'is_completed', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
