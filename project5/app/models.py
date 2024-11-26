from django.db import models
from django.urls import reverse

# Create your models here.
class School(models.Model):
    sname=models.CharField(max_length=100)
    sprincipal=models.CharField(max_length=100)
    def __str__(self):
        return self.sname
    
    def get_absolute_url(self):
        return reverse("schooldetv", kwargs={"pk": self.pk})
    
        


class Student(models.Model):
    stdname=models.CharField(max_length=100)
    stdage=models.IntegerField()
    sname=models.ForeignKey(School,on_delete=models.CASCADE,related_name='schoolstudent')
    def __str__(self):
        return self.stdname
    