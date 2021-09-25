from Apps.home.models import Estudiantes
from django import forms
from .models import Estudiantes, Administradores

class EstudianteForm (forms.ModelForm):
    class Meta:
        model = Estudiantes
        fields = '__all__'

class AdminForm (forms.ModelForm):
    class Meta:
        model = Administradores
        fields = '__all__'