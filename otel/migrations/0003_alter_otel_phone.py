# Generated by Django 5.1.3 on 2024-12-04 14:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otel', '0002_otel_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otel',
            name='phone',
            field=models.CharField(default='+90', max_length=13, validators=[django.core.validators.MinLengthValidator(13, 'Lütfen telefon numarasını alan kodu ile birlikte giriniz.')], verbose_name='Telefon Numarası'),
        ),
    ]