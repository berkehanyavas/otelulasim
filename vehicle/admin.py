from django.contrib import admin
from .models import Vehicle

# Register your models here.

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = [
        'plate',
        'driver',
        'model',
        'max_passenger',
        'owner'
    ]
    class Meta:
        model = Vehicle