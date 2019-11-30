from django.urls import path,re_path
from . import views

app_name = 'main'  # namespace 추가

urlpatterns = [
    path('roomDetail/',views.RoomDetailView.as_view()),
    '''
    path('roomList/<int:pk>', views.SimpleRoomListByActivityView.as_view()),
    re_path(r'^roomList/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$', views.SimpleRoomListByDateView.as_view()),
    path('roomEnter/',views.RoomEnterView.as_view()),
    path('roomCreate/',views.RoomCreateView.as_view()),
    path('roomDetail/',views.RoomDetailView.as_view()),
    path('place/<int:pk>',views.ActivityPlaceView.as_view()),
    '''
]