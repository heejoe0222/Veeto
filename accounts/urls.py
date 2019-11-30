from django.urls import path
from . import views
#from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

app_name = 'accounts'  # namespace 추가

urlpatterns = [
    path('userForm/',views.RegisterForm.as_view()),
]

