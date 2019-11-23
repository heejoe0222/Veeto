from rest_framework import serializers
from .models import User
# from main.serializers import RoomSerializer  #여기서 오류남


# 방 내부의 유저 정보
class UserInfoSerializer(serializers.ModelSerializer):
    age = serializers.ReadOnlyField(source='get_age')
    class Meta:
        fields = ['user_nickname', 'age', 'university', 'self_pr', 'gender', 'profile_image',]
        model = User


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("user_id", "username", "password", "date_of_birth", "gender", "university")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        if self.is_valid(True):
            user = User.objects.create_user(
                user_id=validated_data["user_id"],
                password=validated_data["password"],
                **validated_data
            )
            return user


# 왼쪽 프로필 창에서의 내(로그인중인 유저) 상세 정보
class UserDetailSerializer(serializers.ModelSerializer):
    # rooms = serializers.SerializerMethodField()
    age = serializers.ReadOnlyField(source='get_age')
    class Meta:
        fields = ['user_nickname', 'age', 'university', 'self_pr', 'profile_image', 'university_auth']
        model = User

    # def get_rooms(self, obj):
    #     return RoomSerializer(obj.room_set.all(), many=True) 유저가 참여하는 방 목록