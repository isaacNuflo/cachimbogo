from django.shortcuts import render
from .models import Asignatura, Tema, Subtema, Pregunta
from django.views.decorators.http import require_http_methods
from .forms import UsuarioForm

@require_http_methods(["GET", "POST", "PUT", "DELETE"])
def questionCreate(request):
    asignaturas = Asignatura.objects.all()
    context = {
        'asignaturas' : asignaturas,
    }
    return render(request, 'webadmin/questionCreate.html', context)

def questionBrowser(request):
    asignaturas = Asignatura.objects.all()
    context = {
        'asignaturas' : asignaturas,
    }
    return render(request, 'webadmin/questionBrowser.html', context)

def questionUpdate(request, id):
    pregunta = Pregunta.objects.get(pk=id)
    subtema = Subtema.objects.get(pk=pregunta.id_subtema.id_subtema)
    tema = Tema.objects.get(pk=subtema.id_tema.id_tema)
    subtemas = Subtema.objects.filter(id_tema__id_tema=tema.id_tema)
    temas = Tema.objects.filter(id_asignatura__id_asignatura=tema.id_asignatura.id_asignatura)
    asignaturas = Asignatura.objects.all()
    context = {
        'pregunta': pregunta,
        'tema': tema.id_tema,
        'asignatura': tema.id_asignatura.id_asignatura,
        'subtemas': subtemas,
        'temas': temas,
        'asignaturas': asignaturas,
    }
    return render(request, 'webadmin/questionUpdate.html', context)

def login(request):
    form = UsuarioForm()
    return render(request, 'webadmin/loginForm.html', {'form': form})

