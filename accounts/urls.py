from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

app_name = 'accounts'  # namespace 추가

urlpatterns = [
    path('token-auth/', obtain_jwt_token),  # 로그인: 토큰 발행 with (id, password)
    path('token-refresh/', refresh_jwt_token),  # 토큰 갱신 - 만료되기 전에 가능 with
    path('register/', views.RegisterView.as_view()),
    path('checkDup/', views.checkDuplicate, name='checkDup'),

    path('users/<int:pk>', views.ShowUsersInRoomView.as_view()),
]