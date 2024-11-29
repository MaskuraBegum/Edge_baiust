from django.contrib import admin

# Register your models here.
from .models import Bstudents,Courses,Instructor,Enrollment


admin.site.register(Bstudents)
admin.site.register(Courses)
admin.site.register(Instructor)
admin.site.register(Enrollment)
admin.site.register(studentEnrollment)