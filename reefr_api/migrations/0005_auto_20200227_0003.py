# Generated by Django 2.2 on 2020-02-27 00:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reefr_api', '0004_auto_20200227_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tank',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 2, 27, 0, 3, 58, 325444, tzinfo=utc)),
        ),
    ]