from django import forms
from college.models import *


course_choices = []
for course in Course.objects.all():
    choice = (course.Cid,course.Cname)
    course_choices.append(choice)

subject_choices = []
for subject in Subject.objects.all():
    choice = (subject.subId,subject.subName)
    subject_choices.append(choice)


class StudentAttendanceForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control'}))
    course=forms.ChoiceField(choices=course_choices,widget=forms.Select(attrs={'class':'form-control'}))
    subject=forms.ChoiceField(choices=subject_choices,widget=forms.Select(attrs={'class':'form-control'}))
    
    

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    