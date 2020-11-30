from django import forms
from college.models import CustomUser
from django.contrib.auth.hashers import check_password



class UserLoginForm(forms.Form):
    email = forms.CharField(max_length=150,label=('Email Address'),widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email Address'}))
    password = forms.CharField(max_length=150,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password'}))

    def clean(self):
        email = self.cleaned_data.get('email','')
        password = self.cleaned_data.get('password','')

        if email and password:
            try:
                user = CustomUser.object.get(email=email)
            except:
                raise forms.ValidationError("Email id is doesnot exists !!!!")
            
            if check_password(password,user.password):
                self.cleaned_data['user'] = user
                return self.cleaned_data
            else:
                raise forms.ValidationError("User password is doesnot match !!!")

        else:
            raise forms.ValidationError('Both fields are must required !!!')

    
