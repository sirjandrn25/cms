from django.db import models
from .course import Course


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

class Subject(models.Model):

    subId = models.AutoField(primary_key=True)
    subName = models.CharField(max_length=150)
    degree_level = models.CharField(max_length=150,choices=degree_choices,default=1)
    department = models.CharField(max_length=50,choices=deparment_choices,default=1)


    def __str__(this):
        return this.subName

year_choices = [
    ('1','First Year'),
    ('2','Second Year'),
    ('3','Third Year'),
    ('4','Fourth Year'),
    ('5','Fifth Year')
]
part_choices = [
    ('1','First Part'),
    ('2','Second Part')
]

class SubjectCourse(models.Model):
    
    course = models.ForeignKey(Course,on_delete=models.CASCADE,default=1)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE,default=1)
    year = models.CharField(max_length=10,choices=year_choices,default=1)
    part = models.CharField(max_length=10,choices=part_choices,blank=True,default=1)

    class Meta:
        unique_together = (('course','subject'),)


    def __str__(self):
        return f"{self.course}  {self.subject}"
