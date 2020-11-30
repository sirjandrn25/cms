from django.shortcuts import render,redirect
from django.views import View
from college.models import Subject,SubjectCourse
from college.forms import SubjectForm,AddSubjectForm
from django.contrib import messages
from django.db.models import Q

class SubjectView(View):
    def get(self,request):
        subjects = Subject.objects.all()
        try:
            subject_name=request.GET['subject_name']
            # subjects = Subject.objects.filter(Q(subName__contains=subject_name)|Q(subName=subject_name))
            subjects = Subject.objects.filter(subName__contains=subject_name)

        except:
            pass
        context_data = {
            'subjects':subjects
        }
        return render(request,"subject/index.html",context_data)

class AddSubjectView(View):
    def get(self,request):
        form = SubjectForm()
        context_data = {
            'form':form
        }
        return render(request,"subject/add_new.html",context_data)
    
    def post(self,request):
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,"Subject Add Succesfully")
            return redirect("add_new_subject")
        
        context_data = {
            'form':form
        }
        return render(request,"subject/add_new.html",context_data)


class UpdateSubjectView(View):
    def get(self,request,subject_id):
        subject = Subject.objects.get(subId=subject_id)
        form =SubjectForm(instance=subject)
        
        context_data={
            'form':form,
            'subject_id':subject_id
        }
        return render(request,"subject/update.html",context_data)
    
    def post(self,request,subject_id):
        subject = Subject.objects.get(subId=subject_id)
        form =SubjectForm(instance=subject,data=request.POST)
        
        if form.is_valid():
            update_sub = form.save()
            messages.info(request,f"{update_sub} subject is successfully update")
            return redirect(request.get_full_path())


        context_data={
            'form':form
        }
        return render(request,"subject/update.html",context_data)

class DeleteSubjectView(View):
    def get(self,request,subject_id):
        subject = Subject.objects.get(subId=subject_id)
        return render(request,"subject/confirm_delete.html",{"subject":subject})
    
    def post(self,request,subject_id):
        Subject.objects.get(subId=subject_id).delete()
        return redirect("subject_home")


        
class AddSubjectInCourseView(View):
    def get(self,request):
        form = AddSubjectForm()
        context_data = {
            'form':form
        }
        return render(request,"subject/add_in_course.html",context_data)
    def post(self,request):
        form = AddSubjectForm(request.POST)
        if form.is_valid():
            subject_course = form.save()
            messages.info(request,f"{subject_course.subject} subject add in {subject_course.course} course successfully")
            return redirect("add_subject_course")
        else:
            print("not added")
        
        context_data = {
            'form':form
        }
        return render(request,"subject/add_in_course.html",context_data)


class ViewCoursesOfSubject(View):
    def get(self,request,subject_id):
        objects = SubjectCourse.objects.filter(subject=subject_id)
        context_data = {
            'objects':objects
        }
        return render(request,"subject/view_courses.html",context_data)

