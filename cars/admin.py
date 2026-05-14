# /cars/admin.py

from django.contrib import admin
from cars.models import Car, Brand

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'variation', 'factory_year', 'model_year', 'plate', 'value')
    search_fields = ('brand', 'model', 'variation', 'factory_year', 'model_year', 'plate')

admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)