from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe
# Register your models here.

@admin.register(models.Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['image_view','name', 'brand','location',]
    list_display_links =['name', 'brand','image_view']  

    def image_view(self, obj):
        
        return mark_safe(f'<img src="{obj.image.url}" style="width:100px; height:100px" >')

@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(models.Transmission)
class TransmissionAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(models.Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['image_view', 'title', 'description', 'date_add']

    def image_view(self, obj):
        
        return mark_safe(f'<img src="{obj.image.url}" style="width:100px; height:100px" >')

@admin.register(models.SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ['name', 'link','date_add']

@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['image_view', 'name', 'job','date_add']

    def image_view(self, obj):
        
        return mark_safe(f'<img src="{obj.image.url}" style="width:100px; height:100px; border-radius:50%" >')
    
@admin.register(models.Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ['name','date_add']

@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'description','date_add']

@admin.register(models.Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ['copyrights', 'phone', 'email','date_add']

@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'description','image_view','date_add']

    def image_view(self, obj):
        
        return mark_safe(f'<img src="{obj.image.url}" style="width:100px; height:100px" >')