from django.shortcuts import render,redirect, get_object_or_404
from app_edge.models import Courses
from django.views.generic import ListView
from django.contrib.auth import authenticate, login
from django.contrib import messages
from app_edge.forms import LoginForm, RegistrationForm

class edge_students(ListView):
    model = Courses
    template_name = 'students/studentlist.html'
    context_object_name = 'Courses'

def home(request):
    return render(request,'students/home.html')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.post)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request,user)
                return redireact('home')
            else:
                message.error(request,"Invalid username or password")
        else:
            form = LoginForm()
            return render(request, 'students/login.html',{'form':form})
    return render(request,'students/login.html')


def logout(request):
    logout(request)  # Log the user out
    return redirect('login') 

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.post)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redireact('login')
        else:
            form = RegistrationForm()
            return render(request, 'students/register.html', {'form':form})
    return render(request,'students/register.html')