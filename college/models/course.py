from django.db import models


degree_choices = [
        ('+2','+2'),
        ('developma','Developma'),
        ('bachler','Bachler'),
        ('master','Master')
    ]
deparment_choices = [
        ('science','Science'),
        ('management','Management'),
        ('other','Other')
    ]

class Course(models.Model):
    
    Cid = models.AutoField(primary_key=True)
    course_code = models.CharField(max_length=50,blank=True)
    Cname = models.CharField(max_length=150)
    Cduration = models.IntegerField(default=4)
    degree_level = models.CharField(max_length=150,choices=degree_choices,default=1)
    department = models.CharField(max_length=50,choices=deparment_choices,default=1)
    seats = models.IntegerField(default=48)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    semester = models.BooleanField(default=False)


    def __str__(self):
        return self.Cname
    
