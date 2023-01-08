from django import  forms
from django.core import validators
from edu_app_CRUD import models

class SchoolForm(forms.ModelForm):
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators])
    school_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    principal = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta():
        model = models.SchoolModel
        fields = ['school_name', 'principal', 'location']

class SchoolUpdateForm(forms.ModelForm):
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators])
    school_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    principal = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    #location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta():
        model = models.SchoolModel
        fields = ['school_name', 'principal']

class StudentForm(forms.ModelForm):
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators])
    student_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[validators.MinValueValidator(0)])
    school_name = forms.ModelChoiceField(queryset=models.SchoolModel.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta():
        model = models.StudentModel
        fields = ['student_name', 'age', 'school_name']

class StudentUpdateForm(forms.ModelForm):
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators])
    student_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[validators.MinValueValidator(0)])
    #school_name = forms.ModelChoiceField(queryset=models.SchoolModel.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta():
        model = models.StudentModel
        fields = ['student_name', 'age']
