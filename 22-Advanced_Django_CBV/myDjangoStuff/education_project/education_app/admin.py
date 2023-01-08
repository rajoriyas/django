from django.contrib import admin
from education_app.models import SchoolModel, StudentModel

# Register your models here.
admin.site.register(SchoolModel)
admin.site.register(StudentModel)
