from django.db import models
from django.urls import  reverse

# Create your models here.
class SchoolModel(models.Model):
    school_name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.school_name


    # Have already defined in views.py in CreateView and UpdateView
    def get_absolute_url(self):
        return reverse('edu_app_CRUD:school_detail', kwargs={'pk':self.pk})


class StudentModel(models.Model):
    student_name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school_name = models.ForeignKey(SchoolModel, related_name='students', on_delete=models.CASCADE)

    def __str__(self):
        return self.student_name

    def get_absolute_url(self):
        return reverse('edu_app_CRUD:school_detail', kwargs={'pk':self.school_name.pk})
