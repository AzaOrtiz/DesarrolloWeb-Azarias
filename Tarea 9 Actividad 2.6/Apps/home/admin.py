from django.contrib import admin
from .models import Estudiantes, TipoEstudiante, Articulo, Administradores

# Register your models here.
admin.site.register(Estudiantes)
admin.site.register(TipoEstudiante)
admin.site.register(Articulo)
admin.site.register(Administradores)
