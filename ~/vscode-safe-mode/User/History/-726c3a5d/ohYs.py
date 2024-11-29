from django.shortcuts import render,redirect, get_object_or_404
from app_edge.models import Courses
from django.views.generic import ListView

class edge_students(ListView):
    model = Courses
    template_name = 'students/studentlist.html'
    context_object_name = 'Courses'



def register(request):
    if request.method = 'POST'
    from = RegistrationFrom(request.post)
    
