from Apps.home.forms import EstudianteForm, AdminForm
from Apps.home.forms import Estudiantes, Administradores
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import Administradores, Articulo, Estudiantes
from django.urls import reverse_lazy
from .forms import EstudianteForm
# Create your views here.

class HomeView(TemplateView):
    template_name='index.html'

class EstudView(TemplateView):
    template_name='estudiantes.html'

class AdminView(TemplateView):
    template_name='administradores.html'

class CrearEstud(TemplateView):
    template_name='crear_estudiantes.html'

class CrearAdmin(TemplateView):
    template_name='crear_administradores.html'

class ListarEstud(ListView):
    template_name= 'estudiantes.html'
    model = Estudiantes

    def get_queryset(self):
        return Estudiantes.objects.all()

class ListarAdmin(ListView):
    template_name = 'administradores.html'
    model = Administradores

    def get_queryset(self):
        return Administradores.objects.all()

class Art(ListView):
    template_name = 'Articulos.html'
    model = Articulo

    def get_queryset(self):
        return Articulo.objects.all()


class CrearEstudiantesView(CreateView):
    template_name = 'crear_estudiantes.html'
    form_class = EstudianteForm
    success_url = reverse_lazy('crear_estudiantes')

class CrearAdministrador(CreateView):
    template_name = 'crear_administradores.html'
    form_class = AdminForm
    success_url = reverse_lazy('crear_administradores')
    