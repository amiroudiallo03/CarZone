from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe
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

@admin.register(models.Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image_view']

    def image_view(self, obj):
        
        return mark_safe(f'<img src="{obj.image.url}" style="width:100px; height:100px" >')

@admin.register(models.SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ['name', 'link']

@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'job', 'social_network']
    