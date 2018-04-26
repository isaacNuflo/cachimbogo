from django.conf.urls import include, url
try:
  from django.conf.urls import patterns
except ImportError:
  pass
import django
from django.contrib import admin
from servicios import views
from rest_framework.urlpatterns import format_suffix_patterns

if django.VERSION[1] < 10:
  urlpatterns = patterns('',
  
    url(r'^asignatura/(?P<id>[0-9]+)$', views.AsignaturaAPIView.as_view()),
    url(r'^asignatura/$', views.AsignaturaAPIListView.as_view()),
  
    url(r'^dificultad/(?P<id>[0-9]+)$', views.DificultadAPIView.as_view()),
    url(r'^dificultad/$', views.DificultadAPIListView.as_view()),
  
    url(r'^informacion/(?P<id>[0-9]+)$', views.InformacionAPIView.as_view()),
    url(r'^informacion/$', views.InformacionAPIListView.as_view()),
  
    url(r'^tema/(?P<id>[0-9]+)$', views.TemaAPIView.as_view()),
    url(r'^tema/$', views.TemaAPIListView.as_view()),

    url(r'^tema-asignatura/(?P<id>[0-9]+)$',views.TemaAsignaturaAPIView.as_view),

    url(r'^subtema-tema/(?P<id>[0-9]+)$',views.SubtemaTemaAPIView.as_view()),
  
    url(r'^subtema/(?P<id>[0-9]+)$', views.SubtemaAPIView.as_view()),
    url(r'^subtema/$', views.SubtemaAPIListView.as_view()),
  
    url(r'^tipopregunta/(?P<id>[0-9]+)$', views.TipoPreguntaAPIView.as_view()),
    url(r'^tipopregunta/$', views.TipoPreguntaAPIListView.as_view()),
  
    url(r'^pregunta/(?P<id>[0-9]+)$', views.PreguntaAPIView.as_view()),
    url(r'^pregunta/$', views.PreguntaAPIListView.as_view()),

    url(r'^preguntaT/$', views.PreguntaTAPIListView.as_view()),
  
    url(r'^respuesta/(?P<id>[0-9]+)$', views.RespuestaAPIView.as_view()),
    url(r'^respuesta/$', views.RespuestaAPIListView.as_view()),
  
    url(r'^usuario/(?P<id>[0-9]+)$', views.UsuarioAPIView.as_view()),
    url(r'^usuario/$', views.UsuarioAPIListView.as_view()),
  
    url(r'^usuariohasasignatura/(?P<id>[0-9]+)$', views.UsuarioHasAsignaturaAPIView.as_view()),
    url(r'^usuariohasasignatura/$', views.UsuarioHasAsignaturaAPIListView.as_view()),
  
  )
else:
  urlpatterns = [
  
    url(r'^asignatura/(?P<id>[0-9]+)$', views.AsignaturaAPIView.as_view()),
    url(r'^asignatura/$', views.AsignaturaAPIListView.as_view()),
  
    url(r'^dificultad/(?P<id>[0-9]+)$', views.DificultadAPIView.as_view()),
    url(r'^dificultad/$', views.DificultadAPIListView.as_view()),
  
    url(r'^informacion/(?P<id>[0-9]+)$', views.InformacionAPIView.as_view()),
    url(r'^informacion/$', views.InformacionAPIListView.as_view()),
  
    url(r'^tema/(?P<id>[0-9]+)$', views.TemaAPIView.as_view()),
    url(r'^tema/$', views.TemaAPIListView.as_view()),

    url(r'^tema-asignatura/(?P<id>[0-9]+)$',views.TemaAsignaturaAPIView.as_view()),

    url(r'^subtema-tema/(?P<id>[0-9]+)$',views.SubtemaTemaAPIView.as_view()),
  
    url(r'^subtema/(?P<id>[0-9]+)$', views.SubtemaAPIView.as_view()),
    url(r'^subtema/$', views.SubtemaAPIListView.as_view()),
  
    url(r'^tipopregunta/(?P<id>[0-9]+)$', views.TipoPreguntaAPIView.as_view()),
    url(r'^tipopregunta/$', views.TipoPreguntaAPIListView.as_view()),
  
    url(r'^pregunta/(?P<id>[0-9]+)$', views.PreguntaAPIView.as_view()),
    url(r'^pregunta/$', views.PreguntaAPIListView.as_view()),

    url(r'^preguntaT/$', views.PreguntaTAPIListView.as_view()),
  
    url(r'^respuesta/(?P<id>[0-9]+)$', views.RespuestaAPIView.as_view()),
    url(r'^respuesta/$', views.RespuestaAPIListView.as_view()),
  
    url(r'^usuario/(?P<id>[0-9]+)$', views.UsuarioAPIView.as_view()),
    url(r'^usuario/$', views.UsuarioAPIListView.as_view()),
  
    url(r'^usuariohasasignatura/(?P<id>[0-9]+)$', views.UsuarioHasAsignaturaAPIView.as_view()),
    url(r'^usuariohasasignatura/$', views.UsuarioHasAsignaturaAPIListView.as_view()),
  
  ]
urlpatterns = format_suffix_patterns(urlpatterns)