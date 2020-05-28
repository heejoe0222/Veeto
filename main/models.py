from django.db import models
from accounts.models import TempUser


# 액티비티 (방탈출, 볼링, 보드게임)
class Activity(models.Model):
    name = models.CharField(max_length=20, verbose_name="액티비티 종류")

    def __str__(self):
        return self.name


class RoomCandidate(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.PROTECT)  # 액티비티 종류
    date = models.DateField()  # 활동 날짜
    time = models.TimeField()  # 활동 시간

    def __str__(self):  # 액티비티+활동날짜시간+총인원 표시
        return self.activity.__str__()+"| "+str(self.date)+" "+str(self.time)


class Room(models.Model):
    members = models.ManyToManyField(TempUser, through='RoomUser', through_fields=('room','user'))  # TempUser.room_set 또는 rooms.members
    roomCandidate = models.ForeignKey(RoomCandidate, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id)+" | "+str(self.roomCandidate.activity.name)+" | "+str(self.roomCandidate.date)+" "+str(self.roomCandidate.time)


class RoomUser(models.Model):
    user = models.ForeignKey(TempUser, on_delete=models.PROTECT)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)+" | "+self.room.roomCandidate.__str__()