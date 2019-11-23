from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.settings import api_settings

from rest_framework.exceptions import PermissionDenied, APIException
from django.core.exceptions import ObjectDoesNotExist

from accounts.models import User
from accounts.serializers import UserInfoSerializer, CreateUserSerializer

# 아이디 중복체크 함수
# HTTP GET, /accounts/checkDup/?type={nick or id or email}&word={해당 닉네임 또는 id 또는 email}
def checkDuplicate(request):
    try:
        if request.GET['type'] == 'id':
            user = User.objects.get(user_id=request.GET['word'])
        elif request.GET['type'] == 'nick':
            user = User.objects.get(user_nickname=request.GET['word'])
        elif request.GET['type'] == 'email':
            user = User.objects.get(school_email=request.GET['word'])
    except Exception as e:
        user = None

    if user is None:
        body = {'msg': 'success'}
        return Response(body, status=status.HTTP_200_OK)
    else:
        body = {'msg': 'id already existed'}
        return Response(body, status=status.HTTP_400_BAD_REQUEST)



class ShowUsersInRoomView(generics.RetrieveAPIView):  # user test용
    queryset = User.objects.all()
    serializer_class = UserInfoSerializer


# 회원가입 API
class RegisterView(generics.GenericAPIView):
    serializer_class = CreateUserSerializer
    permissions_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        if len(request.data["username"]) < 2:
            body = {"message": "너무 짧은 이름입니다."}
            return Response(body, status=status.HTTP_400_BAD_REQUEST)
        if len(request.data["password"]) < 8:  # 비밀번호 8자 이상
            body = {"message": "비밀번호가 너무 짧습니다. 최소 8자 이상입니다."}
            return Response(body, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        return Response(
            {
                "user": user.username,
                "token": token,
            },
            status = status.HTTP_201_CREATED
        )

# 추가정보 등록 API (프로필 사진, 해시태그, 닉네임)

# 프로필 사진 변경
# 해시태그 변경


