# Generated by Django 3.0.7 on 2020-11-14 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0002_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default=1, max_length=50),
        ),
    ]
