from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from datetime import date, timedelta, datetime

from accounts.models import SimpleUser
from main.models import Room, Activity, RoomUser
from main.serializers import RoomSerializer, SimpleRoomSerializer, RoomUserSerializer

# 날짜별 액티비티별 방 개수 전송하는 api
# HTTP GET, /api
@api_view(['GET'])
def show_schedule(request):
    if request.method == 'GET':
        today = date.today()
        schedule = []
        for i in range(14):
            roomNum_dict={}
            activity_date = today + timedelta(days=i)
            roomNum_dict["year"] = activity_date.year
            roomNum_dict["month"] = activity_date.month
            roomNum_dict["day"] = activity_date.day

            room_num_list=[]
            activity_num = Activity.objects.all().count()
            for id in range(1,activity_num+1):  # 특정 날짜 -> 액티비티별 생성된 방 개수
                room_num_list.append(Room.objects.filter(date=activity_date, activity=Activity.objects.get(pk=id)).count())
            roomNum_dict["rooms"] = room_num_list
            #schedule[activity_day.strftime('%y%m%d')] = roomNum_list  # 191104 형식
            schedule.append(roomNum_dict)  # 2019-11-04 형식
        return Response(schedule, status=status.HTTP_200_OK)


# 날짜, 액티비티종류(date,pk) 파라미터로 get 요청 받았을 때 -> 해당되는 방들의 SimpleRoomSerializer 전송하는 api
# HTTP GET, /api/roomList?date=%Y-%m-%d&pk=activity_pk_#
class SimpleRoomListView(generics.ListAPIView):
    serializer_class = SimpleRoomSerializer

    def get_queryset(self):
            queryset = Room.objects.all()
            activity_date = self.request.GET.get('date', None)
            activity_pk = self.request.GET.get('pk',None)
            if activity_date is not None and activity_pk is not None:
                #activity_date = datetime.strptime(activity_date, '%y%m%d')
                activity_date = datetime.strptime(activity_date, '%Y-%m-%d')
                queryset = queryset.filter(date=activity_date,activity=Activity.objects.get(pk=int(activity_pk)))
            return queryset


# 참여하기 눌렀을 때 -> 해당 방 pk(+유저정보)와 함께 post 요청 -> RoomUser 관계 생성 + 해당 방 RoomSerializer 전송하는 api
# 방 참여 시 고려해야될 점: 성비, 같은 날짜에 유저의 다른 방 참가 여부, 방의 총 인원 수, RoomUser 관계 이미 있진 않은지? -> 구현해야
# HTTP POST, /api/roomEnter/ with body { "room": room_pk_#, "user": user_pk_# }
class RoomEnterView(generics.CreateAPIView):
    queryset = Room.objects.all()

    def post(self, request, *args, **kwargs):
        ru_serializer = RoomUserSerializer(data=request.data)
        if ru_serializer.is_valid():
            ru_serializer.save()  # RoomUser관계 생성
            room_pk = request.POST.get('room','')
            queryset = self.queryset.get(pk=room_pk)
            return Response(RoomSerializer(queryset).data)  # 해당되는 방의 RoomSerializer 전송
        else:
            return Response(ru_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 방 만들기 눌렀을 때 -> 만드는 방 정보 form+유저정보 post 요청 -> db에서 room & RoomUser 관계 생성 + 생성된 룸 RoomSerializer 전송
# HTTP POST, /api/roomCreate/ with body {form}
class RoomCreateView(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        r_serializer = RoomSerializer(data=request.data)

        if r_serializer.is_valid():
            new_room = r_serializer.save()  # Room 생성
            user_pk = request.POST.get('user', None)

            RoomUser(room= new_room, user=SimpleUser.objects.get(id=user_pk), is_master=True).save() # RoomUser관계 생성
            return Response(RoomSerializer(new_room).data)
        else:
            return Response(r_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 미리보기 눌렀을 때 -> 해당 방 pk(+유저정보)와 함께 get 요청 받음 -> 사용자의 콩 차감 in db + 해당 방 멤버들 조회 후 UserSerializer 전송하는 api




