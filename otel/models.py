from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User

# Create your models here.

class Otel(models.Model):
    name = models.CharField(
        max_length=80,
        null=False,
        blank=False,
        verbose_name='Otel Adı'
    )
    phone = models.CharField(
        max_length=13,
        validators=[MinLengthValidator(13,'Lütfen telefon numarasını alan kodu ile birlikte giriniz.')],
        default='+90',
        null=False,
        blank=False,
        verbose_name='Telefon Numarası'
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name='Oluşturan Kullanıcı',
        related_name='otel_created_by'
    )
    def __str__(self):
        return self.name
    
class Pricing(models.Model):
    otel = models.ForeignKey(
        Otel,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name='Otel',
        related_name='pricing_otel'
    )
    min_people = models.PositiveSmallIntegerField()
    max_people = models.PositiveSmallIntegerField(
        null=True,
        blank=True
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Ücret (Price)'
    )
    currency = models.CharField(
        max_length=3,
        choices=[
            ('USD', 'USD'),
            ('EUR', 'EUR'),
            ('TRY', 'TRY'),
        ],
        default='TRY'
    )
    def __str__(self):
        if self.max_people:
            return f'{self.otel} - {self.min_people}-{self.max_people} -> {self.currency} {self.price}'
        return f'{self.otel} - {self.min_people}+ -> {self.currency} {self.price}'