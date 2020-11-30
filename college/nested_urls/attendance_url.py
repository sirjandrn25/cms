from django.urls import path
from college.views import *


urlpatterns = [
    path('student/',StudentAttendanceView.as_view(),name="student_attendance"),
    path('get_subjects/<int:course_id>/',get_subjects,name="get_subjects"),
]
