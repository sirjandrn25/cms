from django.views import View
from django.shortcuts import render,redirect,HttpResponse
from college.forms import *
from college.models import *
import datetime
from django.contrib import messages
from django.http import JsonResponse



def subject_lists(course):
    subject_course=SubjectCourse.objects.filter(course=course)
    subject_list=[]
    for sc in subject_course:
        data ={
            'id':sc.subject.subId,
            'name':sc.subject.subName
        }
        subject_list.append(data)
    

    return subject_list

def subject_choices(subject_list):
    result_list = []
    for subject in subject_list:
        data = (subject['id'],subject['name'])
        result_list.append(data)
    print(result_list)
    return result_list



class StudentAttendanceView(View):
    def get(self,request):
        admissions = None
        form = StudentAttendanceForm()
        course=None
        date_subject_course = None
        error=None
        form.fields['date'].initial=datetime.datetime.now().date()
        try:
            course_id = request.GET['course']
            subject_id = request.GET['subject']
            date=request.GET['date']
            course = Course.objects.get(Cid=course_id)
            subject = Subject.objects.get(subId = subject_id)
            admissions = Admission.objects.filter(course=course)
            form.fields['course'].initial=(course.Cid,course.Cname)
            subject_list=subject_lists(course)
        

            form.fields['subject'].choices = subject_choices(subject_list)
            
            form.fields['subject'].initial=(subject.subId,subject.subName)
            form.fields['date'].initial = date
            date_subject_course={
                'date':date,
                'subject':subject,
                'course':course
            }
        except Exception as e:
            pass
        if admissions is not None and len(admissions) == 0:
            error=f"students are not found in  {course} course"

        

        context_data = {
            'error':error,
            'form':form,
            'admissions':admissions,
            'date_subject_course':date_subject_course
        }
        return render(request,"attendance/student_attendance.html",context_data)
    
    def post(self,request):
        data = dict(request.POST)
        course_id = int(data.get('course')[0])
        subject_id = int(data.get('subject')[0])
        date = datetime.datetime.strptime(data.get('date')[0],'''%Y-%m-%d''').date()
        course=Course.objects.get(Cid=course_id)
        subject=Subject.objects.get(subId=subject_id)
        
        data.pop('csrfmiddlewaretoken')
        data.pop('course')
        data.pop('subject')
        data.pop('date')
        student_ids = list(map(int,list(data.keys())))
        for student_id in student_ids:
            student=Student.objects.get(StuId=student_id)
            try:
                attendance = StudentAttendance(student=student,course=course,subject=subject,date=date)
                attendance.save()
            except:
                pass
        messages.success(request,"Attendacne is successfully save")
        return redirect(request.get_full_path())


def get_subjects(request,course_id):
    course = Course.objects.get(Cid=course_id)
    subject_course=SubjectCourse.objects.filter(course=course)
    subject_list=[]
    for sc in subject_course:
        data ={
            'id':sc.subject.subId,
            'name':sc.subject.subName
        }
        subject_list.append(data)
    

    data = {
        'subjects':subject_list
    }


    return JsonResponse(data)

