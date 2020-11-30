from django.urls import path,include
from .views import *

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('admin_login/',AdminLoginView.as_view(),name="admin_login"),
    path('admin_logout/',AdminLogoutView.as_view(),name="admin_logout"),

    path('student_management/',include('college.nested_urls.student_url')),
    
    path('course_management/',include('college.nested_urls.course_url')),
    path('subject_management/',include('college.nested_urls.subject_url')),
    path('teacher_management/',include('college.nested_urls.teacher_url')),
    path('attendance_management/',include('college.nested_urls.attendance_url')),
]
