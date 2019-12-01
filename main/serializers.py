from rest_framework import serializers
from .models import Room
from accounts.serializers import UserInfoSerializer


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