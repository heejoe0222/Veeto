from django.db import models
from main.models import Room

# Create your models here.
# mvp 구현을 위한 임시 모델 -> 이후 USER 클래스 상속 예정
class SimpleUser(models.Model):
    user_name = models.CharField(max_length=10)
    age = models.IntegerField()
    university = models.CharField(max_length=1)  # H, E, Y, S
    major = models.CharField(max_length=30)
    rooms = models.ManyToManyField(Room)