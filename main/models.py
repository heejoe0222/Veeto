from django.db import models
from accounts.models import TempUser


# 액티비티 (방탈출, 볼링, 보드게임)
class Activity(models.Model):
    name = models.CharField(max_length=20, verbose_name="액티비티 종류")

    def __str__(self):
        return self.name


class RoomCandidate(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.PROTECT)
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

'''
class ActivityPlace(models.Model):
    name = models.CharField(max_length=30)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    info_link = models.URLField(verbose_name="활동장소 링크", max_length=250)

    def __str__(self):
        return self.name


class Room(models.Model):
    room_name = models.CharField(max_length=12, default="액티비티 같이 해요~!")  # 방 이름(소개) - 12자 이내
    members = models.ManyToManyField(User, through='RoomUser', through_fields=('room','user'))  # simpleuser.room_set 또는 rooms.members
    activity = models.ForeignKey(Activity, on_delete=models.PROTECT)
    date = models.DateField()  # 활동 날짜
    time = models.TimeField()  # 활동 시간
    place = models.ForeignKey(ActivityPlace, on_delete=models.PROTECT)  #활동 장소
    total_number_of_members = models.IntegerField()  # 방 총 인원
    sex_ratio = models.IntegerField(default=0)  # 성비 맞출지 여부 (0-무관, 1-성비맞춤, 2-같은성별만)
    is_Confirm = models.BooleanField(default=False)  # 방 확정여부

    def __str__(self):  # 액티비티+활동날짜시간+총인원 표시
        return self.activity.__str__()+"/ "+str(self.date)+" "+str(self.time)+"("+str(self.total_number_of_members)+")"

    def get_number_of_members(self):
        return self.members.count()

    class Meta:
        ordering = ['date', 'time']


class RoomUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    is_master = models.BooleanField(default=False)
'''