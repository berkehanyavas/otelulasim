from django.db import models
from django.contrib.auth.models import User
from otel.models import Otel

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE, ## bu cascade'lerin üzerine düşün, kullanıcı silindiğinde, otomatik olarak nickname yazsın. null yazmasın.
        null = False,
        blank = False,
        verbose_name= 'Kullanıcı',
        related_name= 'userprofile'
    )
    is_admin = models.BooleanField(
        default=False
    )
    otel = models.ForeignKey(
        Otel,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Kayıtlı Olduğu Otel',
        related_name='user_otel'
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Oluşturan Kullanıcı',
        related_name='created_by'
    )
    is_forgot_pw = models.BooleanField(
        default=False
    )
    created_date = models.DateTimeField(
        auto_now_add=True
    )
    is_deleted = models.BooleanField(
        default=False
    )
    
    def __str__(self):
        return self.user.username