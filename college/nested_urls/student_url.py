from django.urls import path
from college.views.student import *

urlpatterns = [
    path('',StudentView.as_view(),name="student_home"),
    path('admission/',StudentAdmissionView.as_view(),name="admission"),
    path('<int:student_id>/delete/',StudentDeleteView.as_view(),name="delete_student"),
    path('<int:student_id>/update/',StudentUpdateView.as_view(),name="update_student")

]
