from django.urls import path
from .views import index, agregar_piloto, buscar_bd

urlpatterns = [
    path('', index, name='index'),
    path('agregar_piloto/', agregar_piloto, name='agregar_piloto'),
    path('buscar_bd/', buscar_bd, name='buscar_bd'),
    # Agregar más URLs según sea necesario
]