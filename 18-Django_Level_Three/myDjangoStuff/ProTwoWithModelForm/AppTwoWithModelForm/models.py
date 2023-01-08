from django.db import models

# Create your models here.
class myModel(models.Model):
    name = models.CharField(max_length=256, unique=False)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
