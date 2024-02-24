from rest_framework import serializers
from .models import Curso

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'