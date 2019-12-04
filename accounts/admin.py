from django.contrib import admin
from .models import TempUser, University, registerForm, StudentCardImage

# Register your models here.
admin.site.register(TempUser)
admin.site.register(University)
admin.site.register(registerForm)
admin.site.register(StudentCardImage)