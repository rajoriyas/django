from django.shortcuts import render

# Create your views here.
def help(request):
    my_dict = {
        'help_insert':"We're happy to help you"
    }
    return render(request, 'help/index.html', context = my_dict)
