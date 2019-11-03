import json
from rest_framework import generics, status
from rest_framework.decorators import api_view

from datetime import date, timedelta, datetime

from rest_framework.response import Response

from main.models import Room, Activity, RoomUser
from main.serializers import RoomSerializer, SimpleRoomSerializer, RoomUserSerializer

# 날짜별 액티비티별 방 개수 전송하는 api
# HTTP GET, /api
@api_view(['GET'])
def show_schedule(request):
    if request.method == 'GET':
        today = date.today()
        schedule = {}
        for i in range(5):  # date range (지금은 2주, 14일이 default)
            roomNum_list=[]
            activity_date = today + timedelta(days=i)
            roomNum_list.append(activity_date.weekday())  # 날짜에 대한 요일 표시
            room_num_set={}
            activity_num = Activity.objects.all().count()
            for id in range(1,activity_num+1):  # 특정 날짜 -> 액티비티별 생성된 방 개수
                room_num_set[id] = Room.objects.filter(date=activity_date, activity=Activity.objects.get(pk=id)).count()
            roomNum_list.append(room_num_set)
            #schedule[activity_day.strftime('%y%m%d')] = roomNum_list  # 191104 형식
            schedule[str(activity_date)] = roomNum_list  # 2019-11-04 형식
        return Response(schedule, status=status.HTTP_200_OK)


# 날짜, 액티비티종류(date,pk) 파라미터로 get 요청 받았을 때 -> 해당되는 방들의 SimpleRoomSerializer 전송하는 api
# HTTP GET, /api/roomList?date=%Y-%m-%d&pk=activity_pk_#
class SimpleRoomListView(generics.ListAPIView):
    serializer_class = SimpleRoomSerializer

    def get_queryset(self):
        # if self.request.method == 'GET':
            queryset = Room.objects.all()
            activity_date = self.request.GET.get('date', None)
            activity_pk = self.request.GET.get('pk',None)
            if activity_date is not None and activity_pk is not None:
                #activity_date = datetime.strptime(activity_date, '%y%m%d')
                activity_date = datetime.strptime(activity_date, '%Y-%m-%d')
                queryset = queryset.filter(date=activity_date,activity=Activity.objects.get(pk=int(activity_pk)))
            return queryset


# 참여하기 눌렀을 때 -> 해당 방 pk(+유저정보)와 함께 post 요청 -> RoomUser관계 생성 + 해당 방 RoomSerializer 전송하는 api
# 방 참여 시 고려해야될 점: 성비, 같은 날짜에 유저의 다른 방 참가 여부, 방의 총 인원 수, RoomUser 관계 이미 있진 않은지? -> 구현해야
# HTTP POST, /api/roomEnter/ with body { "room": room_pk_#, "user": user_pk_# }
class RoomEnterView(generics.CreateAPIView):
    queryset = Room.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = RoomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # RoomUser관계 생성
            room_pk = request.POST.get('room','')
            queryset = self.queryset.get(pk=room_pk)
            return Response(RoomSerializer(queryset).data)  # 해당되는 방의 RoomSerializer 전송

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 방 만들기 눌렀을 때 -> 만드는 방 정보 form+유저정보 post 요청 -> db에서 room & join 생성 + 생성된 룸 RoomSerializer 전송

# 미리보기 눌렀을 때 -> 해당 방 pk(+유저정보)와 함께 get 요청 받음 -> 사용자의 콩 차감 in db + 해당 방 멤버들 조회 후 UserSerializer 전송하는 api




