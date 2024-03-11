
from django.shortcuts import render

def index(request):
    return render(request, 'nombre_del_nuevo_template/index.html')

from .models import Piloto, Circuito, Carrera
from .forms import PilotoForm, CircuitoForm, CarreraForm

def index(request):
    pilotos = Piloto.objects.all()
    circuitos = Circuito.objects.all()
    carreras = Carrera.objects.all()
    return render(request, 'index.html', {'pilotos': pilotos, 'circuitos': circuitos, 'carreras': carreras})

def agregar_piloto(request):
    if request.method == 'POST':
        form = PilotoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PilotoForm()
    return render(request, 'agregar_piloto.html', {'form': form})

def buscar_bd(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')
        resultados_pilotos = Piloto.objects.filter(nombre__icontains=query)
        resultados_circuitos = Circuito.objects.filter(nombre__icontains=query)
        resultados_carreras = Carrera.objects.filter(nombre__icontains=query)
        return render(request, 'buscar_bd.html', {'resultados_pilotos': resultados_pilotos, 'resultados_circuitos': resultados_circuitos, 'resultados_carreras': resultados_carreras})