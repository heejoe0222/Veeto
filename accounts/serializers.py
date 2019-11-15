from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    age = serializers.ReadOnlyField(source='get_age')
    class Meta:
        fields = ['user_nickname', 'age', 'university', 'self_pr', 'gender', 'profile_image',]
        model = User