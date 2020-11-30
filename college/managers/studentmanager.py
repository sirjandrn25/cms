from django.db import models,connection


#  first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     birth_date = models.DateField()
#     address = models.CharField(max_length=150)
#     phone_no = models.CharField(max_length=15)
#     email = models.EmailField(max_length=150,blank=True)
#     avata

class StudentManager(models.Manager):

    def get_sorting_by_name(self,name=None):
        with connection.cursor() as cursor:
            cursor.execute("select * from college_student order by first_name")
            result_list = []
            for row in cursor.fetchall():
                p = self.model(StuId=row[0],first_name=row[1],last_name=row[2],birth_date=row[3],address=row[4],phone_no=row[5],email=row[6],avatar=row[7])
                result_list.append(p)
            return result_list

    def fileter_by_name(self,name=None):
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM college_student where first_name={name}")
            result_list = []
            for row in cursor.fetchall():
                p = self.model(StuId=row[0],first_name=row[1],last_name=row[2],birth_date=row[3],address=row[4],phone_no=row[5],email=row[6],avatar=row[7])
                result_list.append(p)
            return result_list
    def filter_by_course(self,course=None,name=None):
        if name:
            arr_name = name.split(' ')
        
        with connection.cursor() as cursor:
            if course and name:
                if len(arr_name)>1:
                    cursor.execute(f"SELECT * FROM college_student where (StuId IN (SELECT student_id FROM college_admission WHERE course_id = (SELECT Cid FROM college_course WHERE Cname='{course}'))) and (first_name like '%{arr_name[0]}%' or last_name like '%{arr_name[1]}%')")
                else:
                    cursor.execute(f"SELECT * FROM college_student where (StuId IN (SELECT student_id FROM college_admission WHERE course_id = (SELECT Cid FROM college_course WHERE Cname='{course}'))) and (first_name like '%{name}%' or last_name like '%{name}%')")
            elif course and name is None:
                print("we have got it")

                cursor.execute(f"select * from college_student where StuId in (select student_id from college_admission where course_id in (select Cid from college_course where Cname='{course}')) order by college_student.first_name")
                print("we all right")
            elif course is None and name:
                if len(arr_name)>1:
                    cursor.execute(f'''select * from college_student where (first_name like "%{arr_name[0]}%" or last_name = "%{arr_name[1]}%")''')
                else:
                    cursor.execute(f'''select * from college_student where (first_name like "%{name}%" or last_name = "%{name}%")''')

            else:
                cursor.execute(f"SELECT * FROM college_student")
            result_list = []
            for row in cursor.fetchall():
                p = self.model(StuId=row[0],first_name=row[1],last_name=row[2],birth_date=row[3],address=row[4],phone_no=row[5],email=row[6],avatar=row[7])
                result_list.append(p)
            return result_list

            
