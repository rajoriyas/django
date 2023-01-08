from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import (
                                TemplateView,
                                ListView,
                                DetailView,
                                CreateView,
                                UpdateView,
                                DeleteView
)
from edu_app_CRUD import models
from edu_app_CRUD import forms

# Create your views here.
class IndexView(TemplateView):
    template_name = 'public_html/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        return context

class SchoolListView(ListView):
    model = models.SchoolModel
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'List View'
        return context

class SchoolDetailView(DetailView):
    model = models.SchoolModel
    context_object_name = 'schoolmodel_detail'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detail View'
        return context
"""
class SchoolCreateView(CreateView):
    # default template path = 'app_name/templates/app_name/'
    # default template = 'modelname_form.html'
    # template_name = 'varriable_name'

    model = models.SchoolModel

    # don't want to modify form then form_class varriable is not required.
    form_class = forms.SchoolForm

    # don't need to modify form then fields varriable is required.
    #fields = ['school_name', 'principal', 'location']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # change default context
        context['school_form'] = self.form_class()
        #context['school_form'] = context['form']
        context['title'] = 'Create View'
        return context
"""

def create(request):
    if request.method == 'POST' and 'school_val' in request.POST:
        student_form = forms.StudentForm()
        school_form = forms.SchoolForm(data=request.POST)
        if school_form.is_valid():
            school = school_form.save(commit=True)
            school.save()
            return HttpResponseRedirect(reverse_lazy('edu_app_CRUD:school_detail', args=[school.pk]))
            #return HttpResponseRedirect(reverse('edu_app_CRUD:school_detail', kwargs={'pk': school.id}))
        else:
            print(school_form.errors)

    elif request.method == 'POST' and 'student_val' in request.POST:
        school_form = forms.SchoolForm()
        student_form = forms.StudentForm(data=request.POST)
        if student_form.is_valid():
            student = student_form.save(commit=True)
            student.save()
            return HttpResponseRedirect(reverse_lazy('edu_app_CRUD:school_detail', args=[student.school_name.pk]))
        else:
            print(student_form.errors)
    else:
        school_form = forms.SchoolForm()
        student_form = forms.StudentForm()
    context = {
        'school_form': school_form,
        'student_form': student_form,
        'title': 'Create View'
    }
    return render(request, 'edu_app_CRUD/schoolmodel_form.html', context)


class SchoolUpdateView(UpdateView):
    model = models.SchoolModel
    form_class = forms.SchoolUpdateForm
    # fields = ['school_name', 'principal']

    # default template is modelname_form.html

    # to redirect use models.py, use method get_absolute_url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # change default context
        context['school_form'] = context['form']
        context['title'] = 'Update View'
        return context

class StudentUpdateView(UpdateView):
    model = models.StudentModel
    form_class = forms.StudentUpdateForm
    template_name = 'edu_app_CRUD/schoolmodel_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # change default context
        context['student_form'] = context['form']
        context['title'] = 'Update View'
        return context

class SchoolDeleteView(DeleteView):
    model = models.SchoolModel
    success_url = reverse_lazy('edu_app_CRUD:school_list')

    # template_name works here
    # default template is modelname_confirm_delete.html

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete View'
        return context

class StudentDeleteView(DeleteView):
    model = models.StudentModel
    #success_url = reverse_lazy('edu_app_CRUD:school_list')

    def get_success_url(self):
        school_name = self.object.school_name
        return reverse_lazy('edu_app_CRUD:school_detail', kwargs={'pk':school_name.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Modify View'
        return context
