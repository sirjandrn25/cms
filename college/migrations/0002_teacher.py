# Generated by Django 3.0.7 on 2020-11-14 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=150)),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=50)),
                ('address', models.CharField(max_length=150)),
                ('phone_no', models.CharField(max_length=15)),
                ('salary', models.FloatField()),
                ('degree', models.CharField(choices=[('bachler', (('be', 'BE'), ('bsc', 'BSC'), ('bba', 'BBA'), ('other', 'other'))), ('master', (('me', 'ME'), ('msc', 'MSC'), ('mbs', 'MBS'), ('mba', 'MBA'), ('other', 'other')))], max_length=150)),
            ],
        ),
    ]
