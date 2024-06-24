# personas/urls.py
from django.urls import path
from .views import (
    PersonaListView,
    PersonaDetailView,
    PersonaCreateView,
    PersonaUpdateView,
    PersonaDeleteView,
    crear_persona
)

app_name = 'personas'

urlpatterns = [
    path('', PersonaListView.as_view(), name='lista'),
    path('<int:pk>/', PersonaDetailView.as_view(), name='detalle'),
    path('crear/', PersonaCreateView.as_view(), name='crear'),
    path('editar/<int:pk>/', PersonaUpdateView.as_view(), name='editar'),
    path('borrar/<int:pk>/', PersonaDeleteView.as_view(), name='borrar'),
    path('crear-persona/', crear_persona, name='crear_persona'),
]
