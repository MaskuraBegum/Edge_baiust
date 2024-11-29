from .views.cviews import edge_students,register,login,logout
from django.urls import path

urlpatterns = [
    path('cbv/', edge_students.as_view(), name='edge_students'),
    path('register/', register, name='register'),  # User registration
    path('login/', login, name='login'),  # User login
    path('logout/', logout, name='logout'),  # User logout
    

]