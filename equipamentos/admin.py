from django.contrib import admin
from .models import Equipment


@admin.register(Equipment)
class EquipamentAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'id_code', 
        'brand', 
        'manufecturer', 
        'model', 
        'serial_number',
        'purchase_date',
        'purchase_value',
        'status',
        'maintenance_period',
        'last_maintenance_date',
        'notes',
        'created_at'
        )