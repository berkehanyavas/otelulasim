from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Vehicle(models.Model):
    plate = models.CharField(
        max_length=20,
        verbose_name='Ulaşım Aracı Plakası',
        null=False,
        blank=False
    )
    driver = models.CharField(
        max_length=80,
        verbose_name='Şoför Adı Soyadı',
        null=False,
        blank=False
    )
    model = models.CharField(
        max_length=50,
        verbose_name='Ulaşım Aracı Modeli',
        null=False,
        blank=False
    )
    max_passenger = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(100)],
        verbose_name='Maksimum Yolcu Sayısı'
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name='Sahibi'
    )
    
    def __str__(self):
        return f'{self.plate} - {self.driver} - {self.model}'