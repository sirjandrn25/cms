from django.db import models
from college.models import *


gender_choices = (
    ('male','Male'),
    ('female','Female')
)

degree_choices = (
    ('bachler',
        (
            ('be','BE'),
            ('bsc','BSC'),
            ('bba','BBA'),
            ('other','other')
        )
    ),
    ('master',
        (
            ('me','ME'),
            ('msc','MSC'),
            ('mbs','MBS'),
            ('mba','MBA'),
            ('other','other')
        )
    )
)

class Teacher(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=150)
    birth_date = models.DateField()
    gender = models.CharField(max_length=50,choices=gender_choices,default=1)
    address = models.CharField(max_length=150)
    phone_no = models.CharField(max_length=15)
    salary = models.FloatField()
    degree = models.CharField(max_length=150,choices=degree_choices)
    avatar=models.ImageField(upload_to="avatar/",default="images/default/default-user-img.png")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class TeacherRegisterCourse(models.Model):
    teacher = models.OneToOneField(Teacher,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    join_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.teacher.first_name} {self.teacher.last_name} join {self.course.Cname}"
    

class AssignSubject(models.Model):
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    class Meta:
        unique_together=('teacher','subject','course')

