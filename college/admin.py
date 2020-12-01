from django.contrib import admin

# Register your models here.
# accounts.admin.py

from django.contrib import admin
# from django.contrib.auth.models import Group
# from college.models import CustomUser
from college.models import *

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','email','is_staff','is_admin','is_active']



@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['Cid','Cname','Cduration','degree_level','department','seats','created_date','updated_date']
# admin.site.register(Profile)

# from .models import Subject,SubjectCourse,Student,Admission
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['subId','subName']

@admin.register(SubjectCourse)
class SubjectCourseAdmin(admin.ModelAdmin):
    list_display = ['id','course','subject','year','part']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['StuId','first_name','last_name','phone_no','birth_date','avatar']

@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = ['student','course','date','passout']



@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','email','degree']

@admin.register(StudentAttendance)
class StudentAttendanceAdmin(admin.ModelAdmin):
    list_display = ['id','student','course','subject','date']

@admin.register(AssignSubject)
class AssignSubjectAdmin(admin.ModelAdmin):
    list_display = ['id','course','subject','teacher']
    
admin.site.register(TeacherRegisterCourse)


