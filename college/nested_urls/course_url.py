from django.urls import path
from college.views.course import *


urlpatterns = [
    path('',CourseView.as_view(),name="course_home"),
    path("add_new/",AddCourseView.as_view(),name="add_course"),
    path('<course_id>/update/',UpdateCourseView.as_view(),name="update_course"),
    path('<course_id>/delete/',DeleteCourseView.as_view(),name="delete_course"),
    path('<course_id>/syllabus/',CourseSyllabusView.as_view(),name="course_syllabus"),
    path('<course_id>/add_subject/',AddSubjectInCourseView.as_view(),name="add_subject")
]
