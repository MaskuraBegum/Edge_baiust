from django.db import models

# Create your models here.
class Bstudents(models.Model):
    student_id = models.IntegerField(unique=True, primary_key=True,default="sid")
    student_name = models.CharField( max_length=50,default="sid")
    level = models.IntegerField()
    student_email = models.EmailField(max_length=254, unique=True, default="email")


    def __str__(self):
        return str(self.student_name)


class Courses(models.Model):
    course_id = models.CharField(max_length=50,unique=True, primary_key=True)
    course_name = models.CharField(max_length=50)
    descrpition = models.TextField()
    total_class = models.IntegerField()

    def __str__(self):
        return str(self.course_name)

class Instructor(models.Model):
    instructor_id = models.AutoField(primary_key=True)
    instructor_name = models.TextField()
    instructor_email = models.EmailField( max_length=254, unique=True)
    course_taken = models.ForeignKey(Courses,on_delete=models.CASCADE, default='couse_name')
    def __str__(self):
        return str(self.instructor_name)


class Enrollment(models.Model):
    enrollment_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Bstudents, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    enrollment_date = models.DateField()

    def __str__(self):
        return str(self.enrollment_id)
    