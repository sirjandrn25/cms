# Generated by Django 3.0.7 on 2020-11-25 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0009_course_course_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.Course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.Student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.Subject')),
            ],
            options={
                'unique_together': {('student', 'subject', 'date')},
            },
        ),
    ]
