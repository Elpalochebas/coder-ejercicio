from django.shortcuts import render
from . import models

# Create your views here.

def vista_familiares(request):
    
    frutas = [
        'pera', 'naranja',  'sandia', 'mandarina'
    ]

    familiares = models.Familiar.objects.all()


    context = {
        'frutas' : frutas,
        'familiares' : familiares,
        'titulo': 'Lista de familiares',
        'titulo_pagina': 'CoderHouse ejercicio'
    }

    return render(request, 'familiares.html', context )