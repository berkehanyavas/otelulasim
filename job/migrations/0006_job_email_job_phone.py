# Generated by Django 5.1.3 on 2024-12-04 14:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_remove_job_vehicle_job_passenger_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='phone',
            field=models.CharField(default='+90', max_length=13, validators=[django.core.validators.MinLengthValidator(13, 'Lütfen telefon numarasını alan kodu ile birlikte giriniz.')]),
        ),
    ]
