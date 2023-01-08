from django.shortcuts import render
from AppTwoWithModelForm import forms
#from AppTwoWithModelForm.models import myModel

# Create your views here.
def index(request):
    return render(request, 'public_html/index.html')

def model_form_view(request):
    model_form = forms.myModelForm()
    if request.method == 'POST':
        model_form = forms.myModelForm(request.POST)
        if model_form.is_valid():
            print('Form Credientials')
            print('Name:', model_form.cleaned_data['name'])
            print('Email:', model_form.cleaned_data['email'])
            # mymodel = myModel.objects.get_or_create(name=model_form.cleaned_data['name'], email=model_form.cleaned_data['email'])
            # mymodel.save()
            model_form.save(commit=True)

    return render(request, 'public_html/model_form.html', {'model_form': model_form})
