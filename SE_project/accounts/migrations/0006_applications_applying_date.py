# Generated by Django 2.1.7 on 2019-04-28 12:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_applications'),
    ]

    operations = [
        migrations.AddField(
            model_name='applications',
            name='applying_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]