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