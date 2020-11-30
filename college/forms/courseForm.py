from django import forms
from college.models import *


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('Cname','course_code','Cduration','degree_level','department','seats','semester')
        widgets = {
            'Cname':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Course Name'}),
            'course_code':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter course code'}),
            'Cduration':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Course Duration'}),
            'degree_level':forms.Select(attrs={'class':'form-control','placeholder':'Select Level'}),
            'department':forms.Select(attrs={'class':'form-control','placeholder':'Select Deparment'}),
            'seats':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Course Seats'}),
            'semester':forms.CheckboxInput(attrs={'class':'form-check-input'})
        }
        labels = {
            'Cduration':'Course Duration',
            'Cname':'Course Name',
            'semester':'course is semeter wise'
        }

class AddSubjectForm(forms.ModelForm):
    class Meta:
        model = SubjectCourse
        fields = ('course','subject','year','part')
        widgets = {
            'course':forms.Select(attrs={'class':'form-control'}),
            'subject':forms.Select(attrs={'class':'form-control'}),
            'year':forms.Select(attrs={'class':'form-control'}),
            'part':forms.Select(attrs={'class':'form-control'}),


        }
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # print(args)
    
    
    