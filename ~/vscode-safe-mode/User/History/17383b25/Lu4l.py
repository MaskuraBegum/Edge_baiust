from django.db import models

# Create your models here.
class Bstudents(models.Model):
    name = models.CharField( max_length=50)
    sid = models.IntegerField()
    batch = models.CharField(max_length=50)
    level = models.IntegerField()
    term = models.IntegerField()