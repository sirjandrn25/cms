from django.urls import path
from college.views.subject import *


urlpatterns = [
    path('',SubjectView.as_view(),name="subject_home"),
    path('add_new/',AddSubjectView.as_view(),name="add_new_subject"),
    path('<int:subject_id>/update/',UpdateSubjectView.as_view(),name="update_subject"),
    path('<int:subject_id>/delete/',DeleteSubjectView.as_view(),name="delete_subject"),
    path('add_in_course/',AddSubjectInCourseView.as_view(),name="add_subject_course"),
    path('<int:subject_id>/view_courses/',ViewCoursesOfSubject.as_view(),name="view_subject_courses"),
]
