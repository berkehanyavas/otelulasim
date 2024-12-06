from django.contrib import admin
from .models import Job, Passenger

# Register your models here.

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = [
        'created_by__userprofile__otel__name',
        'created_by',
        'location',
        'destination',
        'date',
        'time'
    ]
    
@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    list_display = [
        'job',
        'name',
        'surname'   
    ]