from django.contrib import admin
from .models import UserProfile

# Register your models here.

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'otel',
        'created_by',
        'is_admin',
        # 'is_reseller',
        'is_forgot_pw',
        'is_deleted'
    ]
    list_filter = [
        'is_admin',
        # 'is_reseller',
        'is_forgot_pw',
        'is_deleted',
    ]
    class Meta:
        model = UserProfile