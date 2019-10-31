from django.db import models

# Create your models here.

class Room(models.Model):
    room_master = models.CharField(max_length=15)  # foreign key로 바꿔야 (models.ForeignKey(User, on_delete=models.PROTECT, related_name=room_i_created))
    activity = models.CharField(max_length=1)  # 액티비티 (방탈출 E, 볼링 B, 보드게임 G)
    date = models.DateField()  # 활동 날짜
    time = models.TimeField()  # 활동 시간
    total_number_of_user = models.IntegerField()  # 방 인원
    sex_ratio = models.IntegerField(default=0) # 성비 맞출지 여부
    room_name = models.TextField(max_length=100, default="반갑습니다~")  # 방 이름(소개)
    is_Confirm = models.BooleanField(default=False)