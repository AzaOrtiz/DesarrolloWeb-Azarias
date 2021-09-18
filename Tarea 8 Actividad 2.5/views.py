from Apps.home.models import Estudiantes
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Administradores, Articulo, Estudiantes
# Create your views here.

class HomeView(TemplateView):
    template_name='index.html'

class ListarEstud(ListView):
    template_name = 'Listado.html'
    model = Estudiantes

    def get_queryset(self):
        return Estudiantes.objects.all()

class ListarAdmin(ListView):
    template_name = 'Listado.html'
    model = Administradores

    def get_queryset(self):
        return Administradores.objects.all()

class Art(ListView):
    template_name = 'Articulos.html'
    model = Articulo

    def get_queryset(self):
        return Articulo.objects.all()