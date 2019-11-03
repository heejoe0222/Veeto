from rest_framework import serializers
from .models import SimpleUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = SimpleUser