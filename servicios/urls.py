from django.urls import path
import django
from servicios import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    path('asignatura/<int:id>', views.AsignaturaAPIView.as_view()),
    path('asignatura/', views.AsignaturaAPIListView.as_view()),

    path('dificultad/<int:id>', views.DificultadAPIView.as_view()),
    path('dificultad/', views.DificultadAPIListView.as_view()),

    path('tema/<int:id>', views.TemaAPIView.as_view()),
    path('tema/', views.TemaAPIListView.as_view()),

    path('tema-asignatura/<int:id>',views.TemaAsignaturaAPIView.as_view()),

    path('subtema-tema/<int:id>',views.SubtemaTemaAPIView.as_view()),

    path('subtema/<int:id>', views.SubtemaAPIView.as_view()),
    path('subtema/', views.SubtemaAPIListView.as_view()),

    path('tipopregunta/<int:id>', views.TipoPreguntaAPIView.as_view()),
    path('tipopregunta/', views.TipoPreguntaAPIListView.as_view()),

    path('pregunta/<int:id>', views.PreguntaAPIView.as_view()),
    path('pregunta/', views.PreguntaAPIListView.as_view()),

    path('preguntaT/', views.PreguntaTAPIListView.as_view()),
    path('preguntaT/<int:id>', views.PreguntaTAPIListView.as_view()),

    path('preguntaR/<int:id>', views.PreguntaRAPIListView.as_view()),

    path('respuesta/<int:id>', views.RespuestaAPIView.as_view()),
    path('respuesta/', views.RespuestaAPIListView.as_view()),

    path('usuario/<int:id>', views.UsuarioAPIView.as_view()),
    path('usuario/', views.UsuarioAPIListView.as_view()),

    path('usuarioAsignatura/<int:id>', views.UsuarioAsignaturaAPIView.as_view()),
    path('usuarioAsignatura/', views.UsuarioAsignaturaAPIListView.as_view()),

    path('usuarioTema/<int:id>', views.UsuarioTemaAPIView.as_view()),
    path('usuarioTema/', views.UsuarioTemaAPIListView.as_view()),

    path('usuarioSubtema/<int:id>', views.UsuarioSubtemaAPIView.as_view()),
    path('usuarioSubtema/', views.UsuarioSubtemaAPIListView.as_view()),

  ]
urlpatterns = format_suffix_patterns(urlpatterns)