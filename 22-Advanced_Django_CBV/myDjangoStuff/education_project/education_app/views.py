from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from education_app import models

# Create your views here.
class IndexView(TemplateView):
    template_name = 'public_html/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        return context

class SchoolListView(ListView):
    model = models.SchoolModel

    # default template --> modelname_list.html # modelname is in lower case
    # can manuplate by varriable --> template_name = 'path'

    # default context --> object_list or modelname_list   # context stands for what even is being return by view  # modelname is in lower case
    # can be manuplate by varriable --> conext_object_name = 'varriable_name'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'List View'
        return context

class SchoolDetailView(DetailView):
    model = models.SchoolModel
    
    # default template --> modelname_detail.html    # modelname is in lower case
    # can manuplate by template_name = 'path'
    template_name = 'education_app/school_detail.html'

    # default context --> object or modelname_detail   # context stands for what even is being return by view     # modelname is in lower case
    # can be manuplate by varriable --> conext_object_name = 'varriable_name'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detail View'
        return context
