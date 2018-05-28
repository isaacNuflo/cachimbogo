from django.shortcuts import render
from .models import Asignatura, Tema, Subtema, Pregunta
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def index(request):
    asignaturas = Asignatura.objects.all()
    context = {
        'asignaturas' : asignaturas,
    }
    return render(request, 'webadmin/index.html',context)

def questionBrowser(request):
    asignaturas = Asignatura.objects.all()
    context = {
        'asignaturas' : asignaturas,
    }
    return render(request, 'webadmin/questionBrowser.html',context)

def questionUpdate(request,id):
    pregunta = Pregunta.objects.get(pk=id)
    subtema = Subtema.objects.get(pk=pregunta.subtema_id_subtema.id_subtema)
    tema = Tema.objects.get(pk=subtema.tema_id_tema.id_tema)
    subtemas = Subtema.objects.filter(tema_id_tema__id_tema=tema.id_tema)
    temas = Tema.objects.filter(asignatura_id_asignatura__id_asignatura=tema.asignatura_id_asignatura.id_asignatura)
    asignaturas = Asignatura.objects.all()
    context = {
        'pregunta' : pregunta,
        'tema' : tema.id_tema,
        'asignatura' : tema.asignatura_id_asignatura.id_asignatura,
        'subtemas' : subtemas,
        'temas' : temas,
        'asignaturas' : asignaturas,
    }
    return render(request, 'webadmin/questionUpdate.html',context)