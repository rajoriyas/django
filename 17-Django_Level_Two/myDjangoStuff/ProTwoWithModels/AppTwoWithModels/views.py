from django.shortcuts import render
from django.http import HttpResponse
from AppTwoWithModels.models import User

# Create your views here.
def index(request):
    return HttpResponse('<h1>Hello World!</h1>')

def user(request):
    info = User.objects.all()
    data = {
        'info': info
    }
    return render(request, 'user/index.html', data)
