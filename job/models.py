from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User

# Create your models here.

class Job(models.Model):
    name = models.CharField(
        max_length=80,
        verbose_name='Yolcu Adı (Passenger Name)',
        null=False,
        blank=False
    )
    surname = models.CharField(
        max_length=80,
        verbose_name='Yolcu Soyadı (Passenger Surname)',
        null=False,
        blank=False
    )
    phone = models.CharField(
        verbose_name='Yolcu Telefon Numarası (Passenger Phone Number)',
        max_length=13,
        # validators=[MinLengthValidator(13,'Lütfen telefon numarasını alan kodu ile birlikte giriniz.')],
        default='',
        null=True,
        blank=True
    )
    email = models.EmailField(
        verbose_name='Yolcu Email Adresi (Passenger Email Address)',
        max_length=254,
        blank=True,
        null=True
    )
    location = models.CharField(
        max_length=120,
        verbose_name='Nereden (From)',
        null=False,
        blank=False
    )
    destination = models.CharField(
        max_length=120,
        verbose_name='Nereye (To)',
        null=False,
        blank=False
    )
    date = models.DateField(
        verbose_name='Tarih (Date)',
        null=False,
        blank=False
    )
    time = models.TimeField(
        verbose_name='Saat (Time)',
        null=False,
        blank=False
    )
    passenger_count = models.IntegerField(
        verbose_name='Yolcu Sayısı (Passenger Count)',
        choices=[(i , str(i)) for i in range(1,16)], 
        default=1
    )
    flight_code = models.CharField(
        verbose_name='Uçuş Kodu (Flight Code)',
        max_length=25,
        null=False,
        blank=False
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name='Oluşturan Kullanıcı',
        related_name='job_created_by'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Ücret (Price)'
    )
    currency = models.CharField(
        max_length=3,
        # choices=[
        #     ('USD', 'US Dollar'),
        #     ('EUR', 'Euro'),
        #     ('TRY', 'Turkish Lira'),
        # ],
        # default='TRY'
    )
    completed = models.BooleanField(
        default=False
    )
    
    def __str__(self):
        return f'{self.created_by.userprofile.otel.name}'
    
class Passenger(models.Model):
    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name='Yolculuk',
        related_name='passenger_job'
    )
    name = models.CharField(
        max_length=80,
        verbose_name='Yolcu Adı (Passenger Name)',
        null=False,
        blank=False
    )
    surname = models.CharField(
        max_length=80,
        verbose_name='Yolcu Soyadı (Passenger Surname)',
        null=False,
        blank=False
    )
    # phone = models.CharField(
    #     verbose_name='Yolcu Telefon Numarası (Passenger Phone Number)',
    #     max_length=13,
    #     # validators=[MinLengthValidator(13,'Lütfen telefon numarasını alan kodu ile birlikte giriniz.')],
    #     default='',
    #     null=True,
    #     blank=True
    # )
    # email = models.EmailField(
    #     verbose_name='Yolcu Email Adresi (Passenger Email Address)',
    #     max_length=254,
    #     blank=True,
    #     null=True
    # )
    def __str__(self):
        return f'{self.name} {self.surname} - {self.job}'