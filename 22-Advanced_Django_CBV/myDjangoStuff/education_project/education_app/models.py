from django.db import models

# Create your models here.
class SchoolModel(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class StudentModel(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(SchoolModel, related_name='students', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
