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
