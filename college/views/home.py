from django.shortcuts import render,redirect
from django.views import View
from django.utils.decorators import method_decorator


class HomeView(View):
    def get(self,request):
        
        return render(request,'college/index.html')