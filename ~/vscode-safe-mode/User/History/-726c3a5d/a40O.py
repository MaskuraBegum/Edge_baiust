from django.shortcuts import render,redirect, get_object_or_404
from app_edge.models import Bstudents
from django.views.generic import ListView

class edge_students(ListView):
    model = Bstudents
    template_name = 'studentlist.html'
    context_object_name = 'bstutdents'