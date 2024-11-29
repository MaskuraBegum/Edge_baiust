from django.shortcuts import render,redirect, get_object_or_404
from app_edge.models import Courses
from django.views.generic import ListView
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from app_edge.forms import LoginForm, RegistrationForm,EnrollmentForm

class edge_students(ListView):
    model = Courses
    template_name = 'students/studentlist.html'
    context_object_name = 'Courses'

def home(request):
    records = Courses.objects.all() 
    return render(request,'students/home.html',{'records': records})

def loginV(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
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
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect ('login')
        else:
            form = RegistrationForm()
            return render(request, 'students/register.html', {'form':form})
    return render(request,'students/register.html')

@login_required   
def senrollment(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "please wait for our email for successfull enrollment")
        return redirect ('home')
    else:
        form = RegistrationForm()
        return render(request, 'students/senroll.html', {'form':form})
    return render(request,'students/senroll.html')