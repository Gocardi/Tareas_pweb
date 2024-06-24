from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Persona

class PersonaListView(ListView):
    model = Persona
    template_name = 'personas/persona_list.html'

class PersonaDetailView(DetailView):
    model = Persona
    template_name = 'personas/persona_detail.html'

class PersonaCreateView(CreateView):
    model = Persona
    fields = ['nombre', 'edad', 'email']
    template_name = 'personas/persona_form.html'
    success_url = reverse_lazy('personas:lista')

class PersonaUpdateView(UpdateView):
    model = Persona
    fields = ['nombre', 'edad', 'email']
    template_name = 'personas/persona_form.html'
    success_url = reverse_lazy('personas:lista')

class PersonaDeleteView(DeleteView):
    model = Persona
    template_name = 'personas/persona_confirm_delete.html'
    success_url = reverse_lazy('personas:lista')

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
