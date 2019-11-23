from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

app_name = 'accounts'  # namespace 추가

urlpatterns = [
    path('token-auth/', obtain_jwt_token),  # 토큰 발행 주소
    # path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
]