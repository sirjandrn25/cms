from django.shortcuts import render,redirect
from college.models import *
from django.views import View
from college.forms import *
from django.contrib import messages


class TeacherHome(View):
    def get(self,request):
        teachers = Teacher.objects.all()
        context_data = {
            'teachers':teachers
        }
        return render(request,"teacher/index.html",context_data)


class AddTeacherView(View):
    def get(self,request):
        teacher_form = TeacherForm()
        teacher_registration_course_form = TeacherRegistrationCourseForm()
        context_data = {
            'teacher_form':teacher_form,
            'teacher_registration_course_form':teacher_registration_course_form
        }
        return render(request,"teacher/add_teacher.html",context_data)
    
    def post(self,request):
        teacher_form = TeacherForm(request.POST,files=request.FILES)
        teacher_registration_course_form = TeacherRegistrationCourseForm(request.POST)

        if teacher_form.is_valid() and teacher_registration_course_form.is_valid():
            teacher=teacher_form.save()
            teacher_register_course = teacher_registration_course_form.save(commit=False)
            teacher_register_course.teacher=teacher
            teacher_register_course.save()

            messages.success(request,"Teacher is successfully register ....")
            return redirect(request.get_full_path())
        else:
            print(form.errors)
        context_data = {
            'form':form
        }
        return render(request,"teacher/add_teacher.html",context_data)
        
