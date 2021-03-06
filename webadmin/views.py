from django.shortcuts import render
from .models import Asignatura, Tema, Subtema, Pregunta, Usuario
from django.views.decorators.http import require_http_methods
from .forms import UsuarioLoginForm, UsuarioRegisterForm
from django.shortcuts import redirect
from rest_framework.response import Response

@require_http_methods(["GET", "POST", "PUT", "DELETE"])
def question_create(request):
    #Todas las Asignaturas
    asignaturas = Asignatura.objects.all()
    context = {
        'asignaturas': asignaturas,
    }
    return render(request, 'webadmin/questionCreate.html', context)


def question_browser(request):
    #Todas las Asignaturas
    asignaturas = Asignatura.objects.all()
    context = {
        'asignaturas': asignaturas,
    }
    return render(request, 'webadmin/questionBrowser.html', context)

#Parametro el id de la pregunta
def question_update(request, id):
    pregunta = Pregunta.objects.get(pk=id)
    subtema = Subtema.objects.get(pk=pregunta.id_subtema.id_subtema)
    tema = Tema.objects.get(pk=subtema.id_tema.id_tema)
    #Todos los subtemas relacionados a un tema
    subtemas = Subtema.objects.filter(id_tema__id_tema=tema.id_tema)
    #Todos los temas relacionadas a una asignatura
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
    if request.method == "POST":
        try:
            #Existencia del usuario
            Usuario.objects.get(usuario=request.POST['usuario'], password=request.POST['password']) 
            return redirect('browser')
        except Usuario.DoesNotExist:
            form = UsuarioLoginForm()
            context = {
                "form": form,
                #Lanza el mensaje de fallo de ingreso
                "alert": 1, 
            }
            return render(request, 'webadmin/loginForm.html', context)
    else:
        form = UsuarioLoginForm()
        context = {
            "form": form,
            "alert": 0,
        }
        return render(request, 'webadmin/loginForm.html', context)


def register(request):
    if request.method == "POST":
        try:
            Usuario.objects.get(usuario=request.POST['usuario'])
            form = UsuarioRegisterForm()
            context = {
                "form": form,
                "alert": 1,
            }
            return render(request, 'webadmin/registerForm.html', context)
        except Usuario.DoesNotExist:
            usuario = Usuario(usuario=request.POST['usuario'], password=request.POST['password'],
                              nombres=request.POST['nombres'], apellidos=request.POST['apellidos'],
                              correo=request.POST['correo'], monedas=0)
            #Guarda en la Base de Datos
            usuario.save()
            return redirect('login')

    else:
        form = UsuarioRegisterForm()
        context = {
            "form": form,
            "alert": 0,
        }
        return render(request, 'webadmin/registerForm.html', context)
