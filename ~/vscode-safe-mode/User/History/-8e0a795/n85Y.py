from .views.cviews import edge_students,register,login,logout,home
from django.urls import path

urlpatterns = [
    path('cbv/', edge_students.as_view(), name='edge_students'),
    path('home/', home, name='home'),
    path('register/', register, name='register'),  # User registration
    path('login/', loginV, name='login'),  # User login
    path('logout/', logout, name='logout'),  # User logout
    

]