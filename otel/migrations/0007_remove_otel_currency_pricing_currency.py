# Generated by Django 5.1.3 on 2024-12-06 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otel', '0006_remove_pricing_currency_otel_currency'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='otel',
            name='currency',
        ),
        migrations.AddField(
            model_name='pricing',
            name='currency',
            field=models.CharField(choices=[('USD', 'USD'), ('EUR', 'EUR'), ('TRY', 'TRY')], default='TRY', max_length=3),
        ),
    ]
