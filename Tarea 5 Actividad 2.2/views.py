from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class HomeView(TemplateView):
    template_name='index.html'



class AdminView(TemplateView):
    template_name='Administrador.html'



class EstView(TemplateView):
    template_name='Estudiantes.html'