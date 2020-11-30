from django import template
from college.models import *

register = template.Library()

@register.filter(name="check_attendance")
def check_attendance(date_subject_course,student):
    # print(date_subject_course)
    date = date_subject_course.get('date')
    subject=date_subject_course.get('subject')
    course=date_subject_course.get('course')

    # print(student)
    try:
        # print(date_subject_course.course)
        attendance = StudentAttendance.objects.get(subject=subject,course=course,date=date,student=student)
        print(attendance)
    except:
        return False
    return True