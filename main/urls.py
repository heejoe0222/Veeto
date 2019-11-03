from django.urls import path
from . import views

app_name = 'main'  # namespace 추가

urlpatterns = [
    path('', views.showSchedule),
    path('roomList/', views.SimpleRoomListView.as_view()),
    # path('<int:pk>/', views.DetailPost.as_view()),
]
