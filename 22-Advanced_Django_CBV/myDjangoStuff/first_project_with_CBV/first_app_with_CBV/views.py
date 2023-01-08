from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse

# Create your views here.
"""
def index(request):
    return render(request, 'public_html/index.html', {'title': 'Home'})
"""
"""
class CBView(View):
    def get(self, request):
        return HttpResponse('Hello World!')
"""
class IndexView(TemplateView):
    template_name = 'public_html/index.html'
    # **kwargs takes dictonary
    # *args takes set
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        return context
