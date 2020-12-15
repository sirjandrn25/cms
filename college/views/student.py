from django.shortcuts import render,redirect
from django.views import View
from django.utils.decorators import method_decorator
from college.forms.studentForm import *
from django.contrib import messages
from college.models import *
import datetime



def count_gender(data,gender_type):
    count = 0
    for item in data:
        if item.gender==gender_type:
            count +=1
        
    return count
        

class StudentView(View):
    def get(self,request):
        students = Student.objects.get_sorting_by_name()
        courses = Course.objects.all()
        try:
            search_value = request.GET.get('search_value')
            course = request.GET.get('course')
            print(course,search_value)
            if course=="all" and search_value:
                students = Student.objects.filter_by_course(name=search_value)
            elif course !="all" and search_value:
                print("yes")
                students = Student.objects.filter_by_course(name=search_value,course=course)
            elif course !="all" and search_value =="":
                students = Student.objects.filter_by_course(course=course)
        except:
            pass
     
        context_data = {
            'students':students,
            'courses':courses,
            'total_students':len(students),
            'total_male':count_gender(students,"male"),
            'total_female':count_gender(students,"female")
        }
        return render(request,"student/index.html",context_data)


class StudentAdmissionView(View):
    def get(self,request):
        student_form = StudentForm()
        admission_form = AdmissionForm()
        context_data = {
            'student_form':student_form,
            'admission_form':admission_form
        }
        return render(request,"student/admission.html",context_data)

    def post(self,request):
        student_form = StudentForm(request.POST,files=request.FILES)
        admission_form = AdmissionForm(request.POST)
        if student_form.is_valid() and admission_form.is_valid():
            student = student_form.save()
            admission = admission_form.save(commit=False)
            course = admission.course
            admission_count = Admission.objects.filter(course=course).count()
            rollno = str(datetime.datetime.now().date().year)+course.course_code+'0'+str(admission_count+1)
           
            
            admission.student = student
            admission.rollno = rollno
            admission.save()
            messages.info(request,f"{student} student successfully get admission in  {admission.course} course")
            return redirect(request.get_full_path())

        else:
            print("no")
        
        context_data = {
            'student_form':student_form,
            'admission_form':admission_form
        }
        return render(request,"student/admission.html",context_data)

class StudentDeleteView(View):
    def get(self,request,student_id):
        student = Student.objects.get(StuId=student_id)
        context_data = {
            'student':student
        }
        return render(request,"student/confirm_delete.html",context_data)
    def post(self,request,student_id):
        Student.objects.get(StuId=student_id).delete()
        return redirect("student_home")


class StudentUpdateView(View):
    def get(self,request,student_id):
        student = Student.objects.get(StuId=student_id)
        student_form = StudentForm(instance=student)
        admission = Admission.objects.get(student=student)
        admission_form = AdmissionUpdateForm(instance=admission)
        context_data = {
            'student_form':student_form,
            'admission_form':admission_form,
            'student':student
        }
        return render(request,"student/update.html",context_data)
    
    def post(self,request,student_id):
        student = Student.objects.get(StuId=student_id)
        student_form = StudentForm(instance=student,data=request.POST,files=request.FILES)
        admission = Admission.objects.get(student=student)
        admission_form = AdmissionUpdateForm(instance=admission,data=request.POST)
        if student_form.is_valid() and admission_form.is_valid():
            student_form.save()
            admission_form.save()
            messages.info(request,f"{student} Successfully updated")
            return redirect(request.get_full_path())
        context_data = {
            'student_form':student_form,
            'admission_form':admission_form,
            'student':student
        }
        return render(request,"student/update.html",context_data)
        

        