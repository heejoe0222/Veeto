from rest_framework import serializers
from .models import TempUser, registerForm


# 방 내부의 유저 정보
class UserInfoSerializer(serializers.ModelSerializer):
    gender = serializers.SerializerMethodField()
    university = serializers.SerializerMethodField()
    class Meta:
        fields = ['user_nickname', 'age', 'gender', 'university',]
        model = TempUser

    def get_gender(self,obj):
        if obj.gender == 'F':
            return '여'
        elif obj.gender == 'M':
            return '남'

    def get_university(self,obj):
        from .models import University
        if obj.university == University.objects.get(pk=1):
            return "서강대학교"
        elif obj.university == University.objects.get(pk=2):
            return "연세대학교"
        elif obj.university == University.objects.get(pk=3):
            return "이화여자대학교"
        elif obj.university == University.objects.get(pk=4):
            return "홍익대학교"


# 사용자로부터 신청폼 받을 때 사용
class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = registerForm
        fields = '__all__'


'''
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
'''
