
from django.shortcuts import render
from .models import *


def inicio(requests):
    
    cursos = Curso.objects.filter(price__lte = 5000)
    context = {'cursos':cursos}

    return render(requests,'cursosapp\\inicio.html', context)


def cursos(requests):

    cursos = Curso.objects.all()
    context = {'cursos':cursos}

    return render(requests, 'cursosapp\\cursos.html', context)


def eventos(requests):

    eventos = Evento.objects.all()
    context = {'eventos': eventos}

    return render(requests, 'cursosapp\\eventos.html', context)






# Create your views here.
