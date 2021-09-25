"""Principal Test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.views.generic.list import ListView
from Apps.home.views import HomeView, ListarEstud, EstudView
from django.contrib import admin
from django.urls import path
from .views import AdminView, Art, CrearAdmin, CrearAdministrador, CrearEstud, EstudView, HomeView, ListarAdmin, CrearEstudiantesView, ListarEstud



urlpatterns = [
    path('index/', HomeView.as_view(), name='home'),
    path('estudiantes/', EstudView.as_view(), name='estudiantes'),
    path('listado/', ListarEstud.as_view(), name='estudiantes'),
    path('administradores/', AdminView.as_view(), name='administradores'),
    path('admins/', ListarAdmin.as_view(), name='administradores'),

    path('Articulos/', Art.as_view(), name='Articulos'),
    path('crearA/', CrearAdministrador.as_view(), name='crear_administradores'),
    path('crear/', CrearEstudiantesView.as_view(), name='crear_estudiantes'),
    
]