# Generated by Django 3.0.7 on 2020-11-26 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0012_auto_20201125_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentattendance',
            name='date',
            field=models.DateField(),
        ),
    ]
