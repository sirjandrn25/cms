# Generated by Django 3.0.7 on 2020-11-25 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0010_studentattendance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentattendance',
            name='date',
            field=models.DateField(),
        ),
    ]
