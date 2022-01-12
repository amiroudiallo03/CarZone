from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand','location']

@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(models.Transmission)
class TransmissionAdmin(admin.ModelAdmin):
    list_display = ['name']
