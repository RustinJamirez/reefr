# Generated by Django 2.2 on 2020-02-28 22:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reefr_api', '0019_auto_20200228_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parametermeasurement',
            name='measured_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 28, 22, 34, 30, 813942)),
        ),
    ]
