from college.models import *
from django import forms




class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('first_name','last_name','email','address','birth_date','gender','phone_no','salary','degree','avatar')
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter valid email address'}),
            'address':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter address'}),
            'phone_no':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Phone Number'}),
            'salary':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter First Name'}),
            'degree':forms.Select(attrs={'class':'form-control','placeholder':'Choose Degree'}),
            'birth_date':forms.DateInput(attrs={'class':'form-control','placeholder':'Enter Your birth date'}),
            'avatar':forms.FileInput(attrs={'class':'form-control','placeholder':'select your avatar'}),
            'gender':forms.Select(attrs={'class':'form-control','placeholder':'Choose gender'}),
        }

class TeacherRegistrationCourseForm(forms.ModelForm):
    class Meta:
        model = TeacherRegisterCourse
        fields = ('course',)
        widgets = {
            'course':forms.Select(attrs={'class':'form-control'})
        }
