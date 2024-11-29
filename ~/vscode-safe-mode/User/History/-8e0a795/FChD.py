from .views.cviews import edge_students,register,loginV,logoutU,home,senrollment
from django.urls import path

urlpatterns = [
    path('cbv/', edge_students.as_view(), name='edge_students'),
    path('home/', home, name='home'),
    path('register/', register, name='register'),  # User registration
    path('login/', loginV, name='login'),  # User login
    path('logout/', logoutU, name='logout'),  # User logout
    path('home/enrollment/', senrollment, name='enrollment'),

]