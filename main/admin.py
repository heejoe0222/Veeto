from django.contrib import admin

from .models import Room, RoomUser, Activity, RoomCandidate

# Register your models here.
admin.site.register(Room)
admin.site.register(RoomUser)
admin.site.register(Activity)
admin.site.register(RoomCandidate)