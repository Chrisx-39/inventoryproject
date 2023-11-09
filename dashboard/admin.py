from django.contrib import admin
from .models import Products, Order,Plant
from django.contrib.auth.models import Group

admin.site.site_header = 'Tefoma Inventory Dashboard'

class ProductAdmin(admin.ModelAdmin):
    list_display=('name','brand','model','category',)
    list_filter =['brand']

class PlantAdmin(admin.ModelAdmin):
    list_display=('fleet_code','plant_name','mileage','comments',)
    list_filter =['plant_name']


# Register your models here.

admin.site.register(Products, ProductAdmin)
admin.site.register(Order)
admin.site.register(Plant, PlantAdmin)
admin.site.unregister(Group)

