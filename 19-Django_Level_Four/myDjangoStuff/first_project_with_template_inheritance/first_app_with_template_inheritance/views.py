from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'public_html/index.html', {'title': 'Home'})

def relative(request):
    return render(request, 'public_html/relative.html', {'title': 'Relative'})

def other(request):
    return render(request, 'public_html/other.html', {'title': 'Other'})
