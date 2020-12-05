from django.shortcuts import render,redirect
from college.models import *
from django.views import View
from college.forms import *
from django.contrib import messages
from datetime import datetime


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

class AssignSubjectView(View):
    def get(self,request,teacher_id):
        form = AssignSubjectForm()
        teacher = Teacher.objects.get(id=teacher_id)
        form.fields['teacher'].initial=teacher
        data = AssignSubject.objects.filter(teacher=teacher).order_by('-date')
        courses = Course.objects.all()
        course_id = request.GET.get('course_option')
        if course_id and course_id !="all":
            course = Course.objects.get(Cid=course_id)
            data = AssignSubject.objects.filter(teacher=teacher,course=course).order_by('-date')


        context_data = {
            'form':form,
            'teacher':teacher,
            'data':data,
            'courses':courses
        }
        return render(request,"teacher/assign_teacher.html",context_data)
    def post(self,request,teacher_id):
    
        form = AssignSubjectForm(request.POST)
        teacher = Teacher.objects.get(id=teacher_id)
        # print(form.fields)
        if form.is_valid():
            course = request.POST.get('course')
            subject = request.POST.get('subject')
            

            assign_subject = AssignSubject.objects.filter(course=course,subject=subject,teacher=teacher,date__year=datetime.now().date().year)
            if assign_subject:
                msg = "Already exists"
            else:
                msg = "Successfully assign subject"
                data = form.save()
                
            messages.info(request,msg)

        
        return redirect(request.get_full_path())


class DeleteAssignSubject(View):
    def get(self,request,id):
        try:
            data = AssignSubject.objects.get(id=id)
            data.delete()
            msg = "Successfully deleted"
        except:
            msg = "Deleted operation is not performed"
        messages.info(request,msg)
        return redirect(request.META['HTTP_REFERER'])

        
