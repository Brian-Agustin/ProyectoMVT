from django.shortcuts import render
from AppDatos.models import Datos
from datetime import datetime

# Create your views here.
def familiar(request):
    familiar1 = Datos(parent='Hermano', nombre='Francisco', apellido='Allende', nacimiento=datetime(2014,5,14))
    familiar1.save()

    familiar2 = Datos(parent='Madre', nombre='Vanesa', apellido='Sanchez', nacimiento=datetime(1990,5,3))
    familiar2.save()

    familiar3 = Datos(parent='Padre', nombre='Lolo', apellido='Allende', nacimiento=datetime(1980,2,1))
    familiar3.save()


    contexto = {
        'Francisco': familiar1,
        'Vanesa': familiar2,
        'Lolo': familiar3
    }
    return render(request, 'familia.html', contexto)