from django.contrib import admin
from cars.models import Car, Brand


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        'brand',
        'model',
        'version',
        'model_year',
        'km',
        'value',
        'city',
        'state',
    )
    search_fields = ('model', 'brand__name', 'version', 'city')
    list_filter = ('brand', 'fuel', 'gear', 'body_type', 'accepts_trade')