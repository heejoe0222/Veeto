from rest_framework import generics, status, permissions
from rest_framework.response import Response

from main.models import Room
from main.serializers import RoomSerializer


# 방 상세 페이지 볼 때(문자로 보내 줄 링크) -> room_pk 전송하면 해당하는 RoomSerializer 전송
# HTTP GET, /api/roomDetail/{room}
class RoomDetailView(generics.RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        queryset = Room.objects.all()
        room_pk = self.kwargs.get('room')
        if room_pk is not None:
            queryset = queryset.get(pk=room_pk)
            return Response(RoomSerializer(queryset).data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)