# Generated by Django 2.2 on 2020-02-27 00:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reefr_api', '0003_tank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tank',
            name='created_on',
            field=models.DateField(default=datetime.date.today),
        ),
    ]