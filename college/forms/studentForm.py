from college.models.student import *
from django import forms

#  student = models.OneToOneField(Student,on_delete=models.CASCADE)
#     course = models.ForeignKey(Course,on_delete = models.CASCADE)
#     date = models.DateField(auto_now_add=True)
#     rollno = models.CharField(max_length=100,blank=True)
#     passout = models.BooleanField(default=False)
#     leave = models.BooleanField(default=True)

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('first_name','last_name','birth_date','address','phone_no','email','avatar','gender')
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'}),
            'address':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Address'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Your Email'}),
            'phone_no':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Phone Number'}),
            'birth_date':forms.DateInput(attrs={'class':'form-control','placeholder':'Enter Your Birth date'}),
            'avatar':forms.FileInput(attrs={'class':'form-control'}),
            'gender':forms.Select(attrs={'class':'form-control'})
        }


class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = ('course',)
        widgets = {
            'course':forms.Select(attrs={'class':'form-control','placeholder':'Choose Your Course'})
        }

class AdmissionUpdateForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = ('course','rollno')
        widgets = {
            'course':forms.Select(attrs={'class':'form-control','placeholder':'Choose Your Course'}),
            # 'date':forms.DateInput(attrs={'class':'form-control','placeholder':'Admission Date'}),
            'rollno':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Student Roll Number'}),

        }
      



    