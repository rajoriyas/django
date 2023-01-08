from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {
        'str' : 'Hello World',
        'num' : 100,
    }
    return render(request, 'public_html/index.html', context_dict)
