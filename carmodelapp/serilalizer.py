from rest_framework import serializers
from .models import Car, Owner

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ['id', 'name', 'email']

class CarSerializer(serializers.ModelSerializer):
    # owner = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    owner = serializers.PrimaryKeyRelatedField(queryset=Owner.objects.all(), allow_null=True, required=False)
    
    class Meta:
        model = Car
        fields = ['id', 'name', 'make', 'model', 'year', 'price', 'color', 'owner']
