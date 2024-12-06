# Generated by Django 5.1.3 on 2024-12-05 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0013_job_name_job_surname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passenger',
            name='email',
        ),
        migrations.RemoveField(
            model_name='passenger',
            name='phone',
        ),
        migrations.AddField(
            model_name='job',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Yolcu Email Adresi (Passenger Email Address)'),
        ),
        migrations.AddField(
            model_name='job',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=13, null=True, verbose_name='Yolcu Telefon Numarası (Passenger Phone Number)'),
        ),
    ]
