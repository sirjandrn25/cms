# Generated by Django 3.1.4 on 2020-12-14 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0019_auto_20201205_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default=1, max_length=30),
        ),
    ]