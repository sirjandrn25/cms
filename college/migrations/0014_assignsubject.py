# Generated by Django 3.0.7 on 2020-12-01 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0013_auto_20201126_2254'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.Course')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.Subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.Teacher')),
            ],
            options={
                'unique_together': {('teacher', 'subject', 'course', 'date')},
            },
        ),
    ]
