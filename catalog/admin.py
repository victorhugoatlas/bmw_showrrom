from django.contrib import admin
from .models import VehicleModel

@admin.register(VehicleModel)
class VehicleModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'family', 'subtitle', 'fuel_type', 'is_m_model', 'updated_at')
    list_filter = ('family', 'fuel_type', 'is_m_model')
    search_fields = ('title', 'subtitle')