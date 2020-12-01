from django.urls import path
from college.views.teacher import *


urlpatterns = [
    path('',TeacherHome.as_view(),name="teacher_home"),
    path('add_teacher/',AddTeacherView.as_view(),name="add_teacher"),
    path('assign_subject/<teacher_id>/',AssignSubjectView.as_view(),name="assign_subject")
]
