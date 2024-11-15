from django.db import models

# Create your models here.
class Bstudents(models.Model):
    name = models.CharField( max_length=50)
    sid = models.IntegerField()
    level = models.IntegerField()
    enrolled = models.CharField(max_length=50)
    batch_code = models.CharField(max_length=50)
    ongoing = models.BooleanField(default=true)


    def __str__(self):
        return self.sid