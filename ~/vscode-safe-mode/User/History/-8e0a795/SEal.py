from .views.cviews import edge_students
from django.urls import path

urlpatterns = [
    path('cbv/', edge_students.as_view(), name='edge_students'),
    path()

]