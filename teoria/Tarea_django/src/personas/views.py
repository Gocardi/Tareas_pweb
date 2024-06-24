from django.shortcuts import render, redirect
from .forms import Persona

def crear_persona(request):
    if request.method == 'POST':
        form = PresonaForm(request.POST)
        if form.is_valid():
            #aqui se procesan los datos limpios
            return redirect('personas:lista')
    else:
        form = PersonaForm()
    return render(request, 'personas/persona_form.html', {'form':form})


def persona_detail(request, persona_id):
    persona = Persona.objects.get(id=persona_id)
    return render(request, 'personas/detail.html', {'persona': persona})


def index(request):
    context = {'mensaje': 'Hola, mundo!'}
    return render(request, 'personas/index.html', context)
# Create your views here.
