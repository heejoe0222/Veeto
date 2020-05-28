from django.urls import path
from . import views

app_name = 'accounts'  # namespace 추가

urlpatterns = [
    path('userForm/', views.RegisterForm.as_view(), name='register-user-form'),
]

