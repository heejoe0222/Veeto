from django.urls import path,re_path
from . import views

app_name = 'main'  # namespace 추가

urlpatterns = [
    path('roomDetail/', views.RoomDetailView.as_view()),
]