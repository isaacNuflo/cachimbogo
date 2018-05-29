from django.conf.urls import url
try:
  from django.conf.urls import patterns
except ImportError:
  pass
import django
from servicios import views
from rest_framework.urlpatterns import format_suffix_patterns

if django.VERSION[1] < 10:
  urlpatterns = patterns('',
  
    url(r'^asignatura/(?P<id>[0-9]+)$', views.AsignaturaAPIView.as_view()),
    url(r'^asignatura/$', views.AsignaturaAPIListView.as_view()),
  
    url(r'^dificultad/(?P<id>[0-9]+)$', views.DificultadAPIView.as_view()),
    url(r'^dificultad/$', views.DificultadAPIListView.as_view()),
  
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
    url(r'^preguntaT/(?P<id>[0-9]+)$', views.PreguntaTAPIListView.as_view()),

    url(r'^preguntaR/(?P<id>[0-9]+)$', views.PreguntaRAPIListView.as_view()),
  
    url(r'^respuesta/(?P<id>[0-9]+)$', views.RespuestaAPIView.as_view()),
    url(r'^respuesta/$', views.RespuestaAPIListView.as_view()),
  
    url(r'^usuario/(?P<id>[0-9]+)$', views.UsuarioAPIView.as_view()),
    url(r'^usuario/$', views.UsuarioAPIListView.as_view()),
  
    url(r'^usuarioAsignatura/(?P<id>[0-9]+)$', views.UsuarioAsignaturaAPIView.as_view()),
    url(r'^usuarioAsignatura/$', views.UsuarioAsignaturaAPIListView.as_view()),
  
  )
else:
  urlpatterns = [
  
    url(r'^asignatura/(?P<id>[0-9]+)$', views.AsignaturaAPIView.as_view()),
    url(r'^asignatura/$', views.AsignaturaAPIListView.as_view()),
  
    url(r'^dificultad/(?P<id>[0-9]+)$', views.DificultadAPIView.as_view()),
    url(r'^dificultad/$', views.DificultadAPIListView.as_view()),
  
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
    url(r'^preguntaT/(?P<id>[0-9]+)$', views.PreguntaTAPIListView.as_view()),

    url(r'^preguntaR/(?P<id>[0-9]+)$', views.PreguntaRAPIListView.as_view()),
  
    url(r'^respuesta/(?P<id>[0-9]+)$', views.RespuestaAPIView.as_view()),
    url(r'^respuesta/$', views.RespuestaAPIListView.as_view()),
  
    url(r'^usuario/(?P<id>[0-9]+)$', views.UsuarioAPIView.as_view()),
    url(r'^usuario/$', views.UsuarioAPIListView.as_view()),
  
    url(r'^usuarioAsignatura/(?P<id>[0-9]+)$', views.UsuarioAsignaturaAPIView.as_view()),
    url(r'^usuarioAsignatura/$', views.UsuarioAsignaturaAPIListView.as_view()),

    url(r'^usuarioTema/(?P<id>[0-9]+)$', views.UsuarioTemaAPIView.as_view()),
    url(r'^usuarioTema/$', views.UsuarioTemaAPIListView.as_view()),

    url(r'^usuarioSubtema/(?P<id>[0-9]+)$', views.UsuarioSubtemaAPIView.as_view()),
    url(r'^usuarioSubtema/$', views.UsuarioSubtemaAPIListView.as_view()),
  
  ]
urlpatterns = format_suffix_patterns(urlpatterns)