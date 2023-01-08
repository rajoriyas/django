from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePage(TemplateView):
    template_name = 'public_html/index.html'

class TestView(LoginRequiredMixin, TemplateView):
    template_name = 'public_html/test.html'

def thanks_view(request):
    return render(request, 'public_html/thanks.html')
