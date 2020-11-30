from django import forms
from college.models import Subject,SubjectCourse



class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('subName','department','degree_level')
        widgets = {
            'subName':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Subject Name'}),
            'department':forms.Select(attrs={'class':'custom-select'}),
            'degree_level':forms.Select(attrs={'class':'custom-select'})
        }
        labels = {
            'subName':'Subject Name'
        }


