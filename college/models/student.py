from django.db import models
from .course import Course
from django.db import connection
from college.managers.studentmanager import *
from college.models import *
import datetime



gender_choices = (
    ('male','Male'),
    ('female','Female')
)
class Student(models.Model):
    
    StuId = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    birth_date = models.DateField()
    address = models.CharField(max_length=150)
    phone_no = models.CharField(max_length=15)
    email = models.EmailField(max_length=150,blank=True)
    avatar = models.ImageField(upload_to="avatar/")
    objects = StudentManager()
    gender = models.CharField(max_length=30,choices=gender_choices,default=1)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    @classmethod
    def get_all_student(cls):
        with connection.cursor() as cursor:
            cursor.execute("Select * from college_student")
            row = cursor.fetchall()
        return row



class Admission(models.Model):
    student = models.OneToOneField(Student,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete = models.CASCADE)
    date = models.DateField(auto_now_add=True)
    rollno = models.CharField(max_length=100,blank=True)
    passout = models.BooleanField(default=False)
    leave = models.BooleanField(default=True)


class StudentAttendance(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    date = models.DateField()

    class Meta:
        unique_together = ('student','subject','date')


    
   


