from rest_framework import generics, status
from rest_framework.response import Response

from datetime import date

from accounts.models import User
from main.models import Room, Activity, RoomUser
from main.serializers import RoomSerializer, SimpleRoomSerializer, RoomUserSerializer

# 날짜 get 요청 받았을 때 -> 해당되는 방들의 SimpleRoomSerializer 전송하는 api
# HTTP GET, /api/roomList/{year}/{month}/{day}
class SimpleRoomListByDateView(generics.ListAPIView):
    serializer_class = SimpleRoomSerializer

    def get_queryset(self):
            queryset = Room.objects.all()
            year = self.kwargs.get('year')
            month = self.kwargs.get('month')
            day = self.kwargs.get('day')
            if year is not None and month is not None and day is not None:
                activity_date = date(int(year), int(month), int(day))
                queryset = queryset.filter(date=activity_date)
            return queryset

# 액티비티종류(pk) get 요청 받았을 때 -> 해당되는 방들의 SimpleRoomSerializer 전송하는 api
# HTTP GET, /api/roomList/{pk}
class SimpleRoomListByActivityView(generics.ListAPIView):
    serializer_class = SimpleRoomSerializer

    def get_queryset(self):
        queryset = Room.objects.all()
        activity_pk = self.kwargs.get('pk')
        if activity_pk is not None:
            queryset = queryset.filter(activity=Activity.objects.get(pk=int(activity_pk)))
        return queryset

# 참여하기 눌렀을 때 -> 해당 방 pk(+유저정보)와 함께 post 요청 -> RoomUser 관계 생성 + 방 참여한 결과 status 보내주는 api
# 방 참여 시 고려해야될 점: 성비, 학교 인증, 같은 날짜에 유저의 다른 방 참가 여부, RoomUser 관계 이미 있진 않은지?,사용자의 콩 차감 in db -> 구현해야
# HTTP POST, /api/roomEnter/ with body { "room": room_pk_#, "user": user_pk_# }
class RoomEnterView(generics.CreateAPIView):
    queryset = Room.objects.all()

    def post(self, request, *args, **kwargs):
        ru_serializer = RoomUserSerializer(data=request.data)
        if ru_serializer.is_valid():
            ru_serializer.save()  # RoomUser관계 생성
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(ru_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 방 만들기 눌렀을 때 -> 만드는 방 정보 form+유저정보 post 요청 -> 학교 인증 확인 후 db에서 room & RoomUser 관계 생성 + 방 생성한 결과 status 보내주는 api
# HTTP POST, /api/roomCreate/ with body {form}
class RoomCreateView(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        r_serializer = RoomSerializer(data=request.data)

        if r_serializer.is_valid():
            new_room = r_serializer.save()  # Room 생성
            user_pk = request.POST.get('user', None)
            RoomUser(room= new_room, user=User.objects.get(id=user_pk), is_master=True).save() # RoomUser관계 생성
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(r_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 방 상세 페이지 볼 때(방 만든 후, 방 참가한 후, 방 목록 리스트에서 접근할 때) -> user와 room_pk 전송하면 해당하는 RoomSerializer 전송
# get 요청이 보안 상 괜찮을지..?
# HTTP GET, /api/roomDetail/?user=user_pk_#&room=room_pk_#
class RoomDetailView(generics.RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        queryset = Room.objects.all()
        user_pk = request.GET.get('user', None)
        room_pk = request.GET.get('room', None)
        room_user_q = RoomUser.objects.filter(user=User.objects.get(id=user_pk), room=Room.objects.get(id=room_pk))
        if user_pk is not None and room_pk is not None and room_user_q.count()!=0:
            queryset = queryset.get(pk=room_pk)
            return Response(RoomSerializer(queryset).data)  # 방장 누구인지를 같이 보내줘야되는지, 같이 보낸다면 어떻게 구현할지
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 미리보기 눌렀을 때 -> 해당 방 pk(+유저정보)와 함께 get 요청 받음 -> 사용자의 콩 차감 in db + 해당 방 멤버들 조회 후 UserSerializer 전송하는 api




