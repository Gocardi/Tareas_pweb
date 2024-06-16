from django.shortcuts import render
def persona_detail(request, persona_id):
    persona = Persona.objects.get(id=persona_id)
    return render(request, 'personas/detail.html', {'persona': persona})
def index(request):
    context = {'mensaje': 'Hola, mundo!'}
    return render(request, 'personas/index.html', context)
# Create your views here.
