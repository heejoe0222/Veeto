from django.urls import path
from . import views

app_name = 'main'  # namespace 추가

urlpatterns = [
    path('', views.show_schedule),
    path('roomList/', views.SimpleRoomListView.as_view()),
    path('roomEnter/',views.RoomEnterView.as_view()),
    path('roomCreate/',views.RoomCreateView.as_view()),
    path('roomDetail/',views.RoomDetailView.as_view()),
]
