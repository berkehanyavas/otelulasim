# Generated by Django 5.1.3 on 2024-12-04 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_alter_job_email_alter_job_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='flight_code',
            field=models.CharField(default='', max_length=25, verbose_name='Uçuş Kodu (Flight Code)'),
            preserve_default=False,
        ),
    ]