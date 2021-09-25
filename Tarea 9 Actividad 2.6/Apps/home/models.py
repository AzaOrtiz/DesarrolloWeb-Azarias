from django.db import models
from django.db.models.fields import CharField

class Estudiantes(models.Model):
    carnet = models.CharField(max_length=200)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50) 
    tipo = models.ForeignKey(
        'TipoEstudiante',
        on_delete = models.CASCADE,
        default=1
        )    
    creacion = models.DateField(auto_now_add=True)
    actualizacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s' % (self.nombre)

class TipoEstudiante(models.Model):
    tipo = models.CharField(max_length=30)
    creacion = models.DateField(auto_now_add=True)
    actualizacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s' % (self.tipo)


class Articulo(models.Model):
    titulo = models.CharField(max_length=30)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=200)
    Autoriza = models.ForeignKey(
        'Administradores',
        on_delete = models.CASCADE,
        default=1
        )    
    comentario = models.CharField(max_length=200, default="")
    Estudiantes = models.ManyToManyField(Estudiantes)
    creacion = models.DateField(auto_now_add=True)
    actualizacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s' % (self.titulo)

class Administradores(models.Model):
    nombre = models.CharField(max_length=30)    
    creacion = models.DateField(auto_now_add=True)
    actualizacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s' % (self.nombre)