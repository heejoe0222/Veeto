from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from accounts.models import TempUser
from main.models import RoomCandidate
from accounts.serializers import FormSerializer


# HTTP POST, /accounts/userForm/
# 이미지 주소나 pk 같이 받아서 폼 생성
class RegisterForm(generics.CreateAPIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = FormSerializer(data=request.data)

        if serializer.is_valid():
            form = serializer.save()

            desired_room = RoomCandidate.objects.get(
                activity=serializer.data['activity'],
                date = serializer.data['date'],
                time = serializer.data['time']
            )

            TempUser(
                user_name = form.user_name,
                user_nickname = form.user_nickname,
                age = form.age,
                university = form.university,
                gender = form.gender,
                phone_num = form.phone_num,
                desired_room = desired_room,
                desired_gender_ratio = form.desired_gender_ratio,
                is_photoOK = form.is_photoOK,
            ).save()

            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''
class UpdateAuthImage(generics.UpdateAPIView):
    serializer_class = FormSerializer
    queryset = registerForm.objects.all()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data={"msg":"이미지 업데이트 완료"}, status=status.HTTP_200_OK)
'''



'''
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

'''

