# Generated by Django 3.0.7 on 2020-11-25 08:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0011_auto_20201125_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentattendance',
            name='date',
            field=models.DateField(default=datetime.date(2020, 11, 25)),
        ),
    ]
