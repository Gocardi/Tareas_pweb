from django.urls import path 
from .views import crear_persona

app_name = 'personas'
urlpatterns = [
    path('crear-persona/', crear_persona, name='crear_persona'),
]
