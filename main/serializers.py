from rest_framework import serializers
from .models import Room, RoomUser, ActivityPlace
from accounts.serializers import UserSerializer


class RoomSerializer(serializers.ModelSerializer):
    members = UserSerializer(read_only=True, many=True)
    class Meta:
        fields = '__all__'
        model = Room


class ActivityPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPlace
        field = ('name', 'info_link')


class SimpleRoomSerializer(serializers.ModelSerializer):
    number_of_members = serializers.ReadOnlyField(source='get_number_of_members')
    year = serializers.SerializerMethodField()
    month = serializers.SerializerMethodField()
    day = serializers.SerializerMethodField()
    place = serializers.SerializerMethodField()

    class Meta:
        model = Room
        exclude = ('members', 'date', 'total_number_of_members')

    def get_year(self,obj):
        return obj.date.year

    def get_month(self,obj):
        return obj.date.month

    def get_day(selfs,obj):
        return obj.date.day

    def get_place(self,obj):
        return obj.place.name


class RoomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomUser
        fields = '__all__'




