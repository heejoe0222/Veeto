import json
from rest_framework import generics, status
from rest_framework.decorators import api_view
from django.http import JsonResponse

from datetime import date, timedelta, datetime

from rest_framework.response import Response

from main.models import Room, Activity
from main.serializers import RoomSerializer, SimpleRoomSerializer

# get으로 url 접근 -> 날짜별 액티비티별 방 개수 전송하는 api
@api_view(['GET'])
def showSchedule(request):
    if request.method == 'GET':
        today = date.today()
        schedule = {}
        for i in range(5):  #for i in range(14):
            roomNum_list=[]
            activity_day = today + timedelta(days=i)
            roomNum_list.append(activity_day.weekday())  # 날짜에 대한 요일 표시
            for id in range(1,4):  # 특정 날짜 -> 액티비티별 생성된 방 개수
                roomNum_list.append(Room.objects.filter(date=activity_day, activity=Activity.objects.get(pk=id)).count())
            schedule[activity_day.strftime('%y%m%d')] = roomNum_list
        return JsonResponse(json.dumps(schedule), safe=False)


# 날짜, 액티비티종류(date,pk) 파라미터로 get 요청 받았을 때 -> 해당되는 방들의 SimpleRoomSerializer 전송하는 api
class SimpleRoomListView(generics.ListAPIView):
    serializer_class = SimpleRoomSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = Room.objects.all()
            activity_date = self.request.GET.get('date', None)
            activity_pk = self.request.GET.get('pk',None)
            if activity_date is not None and activity_pk is not None:
                activity_date = datetime.strptime(activity_date, '%y%m%d')
                queryset = queryset.filter(date=activity_date,activity=Activity.objects.get(pk=int(activity_pk)))
            return queryset

# 미리보기 눌렀을 때 -> 해당 방 pk(+유저정보)와 함께 get 요청 받음 -> 사용자의 콩 차감 in db + 해당 방 멤버들 조회 후 UserSerializer 전송하는 api

# 참여하기 눌렀을 때 -> 해당 방 pk(+유저정보)와 함께 post 요청 -> db에서 해당유저 join 생성 + 해당 방 RoomSerializer 전송하는 api

# 방 만들기 눌렀을 때 -> 만드는 방 정보 form+유저정보 post 요청 -> db에서 room & join 생성 + 생성된 룸 RoomSerializer 전송




