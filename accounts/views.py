from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from accounts.models import TempUser
from main.models import RoomCandidate
from accounts.serializers import FormSerializer

from conf.slack import slack_notify

# HTTP POST, /accounts/userForm/
# 액티비티 신청 폼 생성
class RegisterForm(generics.CreateAPIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = FormSerializer(data=request.data)

        if serializer.is_valid():
            form = serializer.save()

            slack_message='USER: {}({}) {} {} \nROOM: {} {}시 {}'.format(
                form.user_name, form.gender, form.university, form.phone_num, form.date.strftime('%Y/%m/%d'), form.time.strftime("%H"), form.activity.__str__()
            )
            slack_notify(slack_message, '#register_alarm', username='뉴비토알림봇')

            # 없는 방이면 만들어서 넣고 아님 찾아서 넣고
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