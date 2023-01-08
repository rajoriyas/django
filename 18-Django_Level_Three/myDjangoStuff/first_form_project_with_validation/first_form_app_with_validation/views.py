from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):
    return render(request, 'index.html')

def base(request):
    form = forms.Base()

    if request.method == 'POST':
        form = forms.Base(request.POST)
        if form.is_valid():
            print('Form Credientials')
            print('Name:', form.cleaned_data['name'])
            print('Email:', form.cleaned_data['email'])
            print('Text:', form.cleaned_data['text'])

    return render(request, 'base/index.html', {'form': form})
