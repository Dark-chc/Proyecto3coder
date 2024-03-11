from django import forms
from .models import Piloto, Circuito, Carrera

class PilotoForm(forms.ModelForm):
    class Meta:
        model = Piloto
        fields = ['nombre', 'equipo', 'puntos']

class CircuitoForm(forms.ModelForm):
    class Meta:
        model = Circuito
        fields = ['nombre', 'pais', 'longitud']

class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = ['nombre', 'fecha', 'circuito']