from django.contrib import admin
from .models import Otel, Pricing

# Register your models here.

@admin.register(Otel)
class OtelAdmin(admin.ModelAdmin):
    list_display = [
        'name'
    ]
    
@admin.register(Pricing)
class PricingAdmin(admin.ModelAdmin):
    list_display = [
        'otel',
        'min_people',
        'max_people',
        'price',
        'currency'
    ]