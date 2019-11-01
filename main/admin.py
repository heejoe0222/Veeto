from django.contrib import admin

from .models import Room, Join, Activity

# Register your models here.
admin.site.register(Room)
admin.site.register(Join)
admin.site.register(Activity)