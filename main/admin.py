from django.contrib import admin

from .models import Room, RoomUser, Activity, ActivityPlace

# Register your models here.
admin.site.register(Room)
admin.site.register(RoomUser)
admin.site.register(Activity)
admin.site.register(ActivityPlace)