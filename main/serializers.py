from rest_framework import serializers
from .models import Room
from accounts.serializers import UserSerializer


class RoomSerializer(serializers.ModelSerializer):
    members = UserSerializer(read_only=True, many=True)
    class Meta:
        fields = '__all__'
        model = Room


class SimpleRoomSerializer(serializers.ModelSerializer):
    number_of_members = serializers.ReadOnlyField(source='get_number_of_members')

    class Meta:
        model = Room
        exclude = ('members','activity','date',)



