from django.shortcuts import render,redirect
from django.views import View
from college.forms import UserLoginForm
from django.contrib import messages
from django.contrib.auth import login,logout


class AdminLoginView(View):
    def get(self,request):
        form = UserLoginForm()
        context = {
            'form':form,
        }

        return render(request,"myadmin/login.html",context)
    
    def post(self,request):
        form = UserLoginForm(request.POST)

        if form.is_valid():
            user = form.cleaned_data['user']
            if user.is_admin:
                login(request,user)
                return redirect("home")
            messages.info(request,"Only admin user is valid")
            return redirect("admin_login")
                
        
        context = {
            'form':form,
        }
        return render(request,"myadmin/login.html",context)


class AdminLogoutView(View):
    def get(self,request):
        logout(request)
        messages.success(request,"User Successfully Logout")
        return redirect("admin_login")