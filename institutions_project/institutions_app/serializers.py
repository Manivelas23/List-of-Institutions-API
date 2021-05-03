from rest_framework import serializers
from .models import institution

class institutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = institution
        fields  = '__all__'
        