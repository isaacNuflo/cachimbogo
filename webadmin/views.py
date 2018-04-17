from django.shortcuts import render
from .models import Asignatura, Tema, Subtema

# Create your views here.
def index(request):
    asignaturas = Asignatura.objects.all()
    temas = Tema.objects.all()
    subtemas = Subtema.objects.all()
    context = {
            'asignaturas' : asignaturas,
            'temas' : temas,
            'subtemas' : subtemas,
    }
    return render(request, 'webadmin/index.html',context)