from django import template
from college.models import *

register = template.Library()

@register.filter(name="get_semester_syllabus")
def get_semester_syllabus(course):
    sc = SubjectCourse.objects.filter(course=course)
    result_list = []
    semester = 1
    for year in range(1,course.Cduration+1):
        for part in range(1,3):
            data = {}
            data['semester'] = semester
            data['items'] = SubjectCourse.objects.filter(course=course,year=year,part=part)
            semester +=1
            result_list.append(data)
        

    return result_list

@register.filter(name="get_level_string")
def get_level_string(level_int):
    if level_int==1:
        return 'first'
    elif level_int==2:
        return 'second'
    elif level_int==3:
        return 'third'
    elif level_int==4:
        return 'fourth'
    elif level_int==5:
        return 'fifth'
    elif level_int==6:
        return 'sixth'
    elif level_int==7:
        return 'seven'
    elif level_int==8:
        return 'eight'
    elif level_int==9:
        return 'nine'
    elif level_int==10:
        return 'ten'

@register.filter(name="get_student_course")
def get_student_course(student):
    admission = Admission.objects.get(student=student)
    return admission.course
    # return True

@register.filter(name="get_teacher_course")
def get_teacher_course(teacher):
    registration=TeacherRegisterCourse.objects.get(teacher=teacher)
    # print(registration.course)
    return registration.course
    # return True

@register.filter(name="get_student_roll")
def get_student_roll(student):
    admission = Admission.objects.get(student=student)
    return admission.rollno
