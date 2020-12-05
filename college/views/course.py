from django.views import View
from college.forms import *
from college.models import *
from django.shortcuts import render,redirect
from django.contrib import messages
from django.db.models import Q

#  fields = ('Cname','Cduration','degree_level','department','seats')
class CourseView(View):
    def get(self,request):
        courses = Course.objects.all()
        try:
            search_value = request.GET['search_value']
            print(Course.objects.filter(department=search_value))
            courses = Course.objects.filter(Q(Cname__contains=search_value)|Q(department=search_value)|Q(degree_level=search_value))
            print(courses)
        except:
            pass
        return render(request,"course/index.html",{"courses":courses})


class AddCourseView(View):
    def get(self,request):
        form = CourseForm()
        context_data = {
            'form':form,
        }
        return render(request,"course/add_new.html",context_data)
    
    def post(self,request):
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,"Course Add Successfully")
            return redirect("add_course")
        
        context_data = {
            'form':form
        }
        return render(request,"course/add_new.html",context_data)


class UpdateCourseView(View):
    def get(self,request,course_id):
        course = Course.objects.get(Cid=course_id)
        form = CourseForm(instance=course)
        context_data = {
            'form':form
        }
        return render(request,"course/update.html",context_data)
    
    def post(self,request,course_id):
        course = Course.objects.get(Cid=course_id)
        form = CourseForm(instance=course,data=request.POST)
        if form.is_valid():
            update_course = form.save()
            messages.info(request,f"{update_course} is successfully updated")
            return redirect(request.get_full_path())
        context_data = {
            'form':form
        }
        return render(request,"course/update.html",context_data)

class DeleteCourseView(View):
    def get(self,request,course_id):
        course = Course.objects.get(Cid=course_id)
        context_data = {
            'course':course
        }
        return render(request,"course/confirm_delete.html",context_data)
    
    def post(self,request,course_id):
        Course.objects.get(Cid=course_id).delete()
        return redirect("course_home")

class CourseSyllabusView(View):
    def get(self,request,course_id):
        course=Course.objects.get(Cid=course_id)
        context_data={
            'course':course
        }
        return render(request,"course/syllabus.html",context_data)
            



def get_years_by_course_duration(course_duration):
    year_choices =[
        ('1','First Year'),
        ('2','Second Year'),
        ('3','Third Year'),
        ('4','Fourth Year'),
        ('5','Fifth Year')
    ]
    
    result_list = []
    for i in range(course_duration):
        result_list.append(year_choices[i])
    
    return result_list


class AddSubjectInCourseView(View):
   
    def get(self,request,course_id):
        course = Course.objects.get(Cid=course_id)
        related_subjects = Subject.objects.filter(degree_level=course.degree_level,department=course.department)
        form = AddSubjectForm()
        form.fields['course'].initial = course
        form.fields['subject'].queryset=related_subjects
        form.fields['year'].choices = get_years_by_course_duration(course.Cduration)
        
        context_data = {
            'form':form,
            'course':course,
        }
        return render(request,"course/add_subject.html",context_data)
    def post(self,request,course_id):

        form = AddSubjectForm(request.POST)
        if form.is_valid():
            try:
                subject_course = form.save()
                messages.info(request,f"{subject_course.subject} subject add in {subject_course.course} course successfully")
            except:
                messages.info(request,"duplicate values is not exists")
            return redirect(request.get_full_path())
        else:
            print("not added")
        
        context_data = {
            'form':form,
            'course_id':course_id
        }
        return render(request,"course/add_subject.html",context_data)