from .views.cviews import edge_students
from django.urls import path

urlpatterns = [
    path('cbv/', edge_students.as_view(), name='edge_students'),
    path('register/', views.cviews.register, name='register'),  # User registration
    path('login/', views.cviews.login, name='login'),  # User login
    path('logout/', views.cvielogout_view, name='logout'),  # User logout
    path('profile/', views.profile_view, name='profile'),  # User profile (secured)
    path('article/create/', views.article_create_view, name='article_create'),

]