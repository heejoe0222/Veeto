from rest_framework import serializers
from .models import Room
from accounts.serializers import UserInfoSerializer



class ActivityPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPlace
        exclude = ('activity',)


class RoomSerializer(serializers.ModelSerializer):
    members = UserInfoSerializer(read_only=True, many=True)
    date = serializers.SerializerMethodField()
    time = serializers.SerializerMethodField()
    activity = serializers.SerializerMethodField()

    class Meta:
        model = Room
        exclude = ('roomCandidate',)

    def get_date(self,obj):
        return obj.roomCandidate.date

    def get_time(self,obj):
        return obj.roomCandidate.time

    def get_activity(self,obj):
        return obj.roomCandidate.activity.id


'''
class SimpleRoomSerializer(serializers.ModelSerializer):
    year = serializers.SerializerMethodField()
    month = serializers.SerializerMethodField()
    day = serializers.SerializerMethodField()

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


class ActivityPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPlace
        exclude = ('activity',)


class RoomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomUser
        fields = '__all__'
'''



