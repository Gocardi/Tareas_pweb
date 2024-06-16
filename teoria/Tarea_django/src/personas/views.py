from django.shortcuts import render

def index(request):
    context = {'mensaje': 'Hola, mundo!'}
    return render(request, 'personas/index.html', context)
# Create your views here.
