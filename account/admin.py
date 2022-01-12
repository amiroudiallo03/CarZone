from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'username', 'password']