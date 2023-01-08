from django.shortcuts import render
from first_form_app import forms
# Create your views here.
def index(request):
    return render(request, 'index.html')

def base_form(request):
    form = forms.Base_Form()

    if request.method == 'POST':
        form = forms.Base_Form(request.POST)
        if form.is_valid():
            print('Validation Successful')
            print('Name: '+form.cleaned_data['name'])
            print('Email: '+form.cleaned_data['email'])
            print('Text: '+form.cleaned_data['text'])

    my_dict = {
        'form': form
    }
    return render(request, 'base_form/index.html', my_dict)
