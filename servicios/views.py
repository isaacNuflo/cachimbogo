from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from servicios.serializers import *
from servicios.models import *
import random

class AsignaturaAPIView(APIView):

    renderer_classes = (JSONRenderer, )
    parser_classes = (JSONParser,)

    def get(self, request, id, format=None):
        try:
            item = Asignatura.objects.get(pk=id)
            serializer = AsignaturaSerializer(item)
            return Response(serializer.data)
        except Asignatura.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Asignatura.objects.get(pk=id)
        except Asignatura.DoesNotExist:
            return Response(status=404)
        serializer = AsignaturaSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Asignatura.objects.get(pk=id)
        except Asignatura.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class AsignaturaAPIListView(APIView):

    renderer_classes = (JSONRenderer, )
    parser_classes = (JSONParser,)

    def get(self, request, format=None):
        items = Asignatura.objects.exclude(pk=19)
        serializer = AsignaturaSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AsignaturaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class DificultadAPIView(APIView):

    renderer_classes = (JSONRenderer, )
    parser_classes = (JSONParser,)

    def get(self, request, id, format=None):
        try:
            item = Dificultad.objects.get(pk=id)
            serializer = DificultadSerializer(item)
            return Response(serializer.data)
        except Dificultad.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Dificultad.objects.get(pk=id)
        except Dificultad.DoesNotExist:
            return Response(status=404)
        serializer = DificultadSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Dificultad.objects.get(pk=id)
        except Dificultad.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class DificultadAPIListView(APIView):

    renderer_classes = (JSONRenderer, )
    parser_classes = (JSONParser,)

    def get(self, request, format=None):
        items = Dificultad.objects.all()
        serializer = DificultadSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DificultadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class SubtemaTemaAPIView(APIView):

    renderer_classes = (JSONRenderer, )
    parser_classes = (JSONParser,)

    def get(self, request, id, format=None):
        try:
            item = Subtema.objects.filter(id_tema__pk=id)
            serializer = SubtemaTemaSerializer(item,many=True)
            return Response(serializer.data)
        except Tema.DoesNotExist:
            return Response(status=404)

class TemaAsignaturaAPIView(APIView):

    renderer_classes = (JSONRenderer, )
    parser_classes = (JSONParser,)

    def get(self, request, id, format=None):
        try:
            item = Tema.objects.filter(id_asignatura__pk=id)
            serializer = TemaAsignaturaSerializer(item,many=True)
            return Response(serializer.data)
        except Tema.DoesNotExist:
            return Response(status=404)

class TemaAPIView(APIView):

    renderer_classes = (JSONRenderer, )
    parser_classes = (JSONParser,)

    def get(self, request, id, format=None):
        try:
            item = Tema.objects.get(pk=id)
            serializer = TemaSerializer(item)
            return Response(serializer.data)
        except Tema.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Tema.objects.get(pk=id)
        except Tema.DoesNotExist:
            return Response(status=404)
        serializer = TemaSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Tema.objects.get(pk=id)
        except Tema.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class TemaAPIListView(APIView):

    renderer_classes = (JSONRenderer, )
    parser_classes = (JSONParser,)

    def get(self, request, format=None):
        items = Tema.objects.all()
        serializer = TemaSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TemaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class SubtemaAPIView(APIView):

    renderer_classes = (JSONRenderer, )
    parser_classes = (JSONParser,)

    def get(self, request, id, format=None):
        try:
            item = Subtema.objects.get(pk=id)
            serializer = SubtemaSerializer(item)
            return Response(serializer.data)
        except Subtema.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Subtema.objects.get(pk=id)
        except Subtema.DoesNotExist:
            return Response(status=404)
        serializer = SubtemaSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Subtema.objects.get(pk=id)
        except Subtema.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class SubtemaAPIListView(APIView):

    renderer_classes = (JSONRenderer, )
    parser_classes = (JSONParser,)

    def get(self, request, format=None):
        items = Subtema.objects.all()
        serializer = SubtemaSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SubtemaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class TipoPreguntaAPIView(APIView):

    renderer_classes = (JSONRenderer, )
    parser_classes = (JSONParser,)

    def get(self, request, id, format=None):
        try:
            item = TipoPregunta.objects.get(pk=id)
            serializer = TipoPreguntaSerializer(item)
            return Response(serializer.data)
        except TipoPregunta.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = TipoPregunta.objects.get(pk=id)
        except TipoPregunta.DoesNotExist:
            return Response(status=404)
        serializer = TipoPreguntaSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = TipoPregunta.objects.get(pk=id)
        except TipoPregunta.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class TipoPreguntaAPIListView(APIView):

    renderer_classes = (JSONRenderer, )
    parser_classes = (JSONParser,)

    def get(self, request, format=None):
        items = TipoPregunta.objects.all()
        serializer = TipoPreguntaSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TipoPreguntaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class PreguntaAPIView(APIView):

    renderer_classes = (JSONRenderer, )
    parser_classes = (JSONParser,)

    def get(self, request, id, format=None):
        try:
            item = Pregunta.objects.get(pk=id)
            serializer = PreguntaSerializer(item)
            return Response(serializer.data)
        except Pregunta.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Pregunta.objects.get(pk=id)
        except Pregunta.DoesNotExist:
            return Response(status=404)
        serializer = PreguntaSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Pregunta.objects.get(pk=id)
        except Pregunta.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class PreguntaTAPIListView(APIView):
    renderer_classes = (JSONRenderer, )
    parser_classes = (JSONParser,)

    def get(self, request, id , format=None):
        items = Pregunta.objects.filter(id_subtema__id_subtema=id)
        serializer = PreguntaTSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PreguntaTSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class PreguntaRAPIListView(APIView):
    renderer_classes = (JSONRenderer,)
    parser_classes = (JSONParser,)

    def get(self, request, id, tipo, format=None):
        items = Pregunta.objects.filter(id_subtema=id, id_tipopregunta=tipo)
        lists = []
        response = []
        if tipo == 1:
            cantidad = 7
        elif tipo == 2:
            cantidad = 10
        else:
            return Response(response)
        i = 1
        while i <= cantidad:
            rand = random.choice(items).id_pregunta
            if not lists:
                lists.append(rand)
                response.append(self.get_answer(rand))
                i = i + 1
            elif rand not in lists:
                lists.append(rand)
                response.append(self.get_answer(rand))
                i = i + 1

        return Response(response)

    def get_answer(self, rand):
        pregunta = Pregunta.objects.get(pk=rand)
        serializer = PreguntaTSerializer(pregunta, many=False)
        return serializer.data

class PreguntaAPIListView(APIView):

    renderer_classes = (JSONRenderer, )
    parser_classes = (JSONParser,)

    def get(self, request, format=None):
        items = Pregunta.objects.all()
        serializer = PreguntaSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PreguntaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class RespuestaAPIView(APIView):

    renderer_classes = (JSONRenderer, )
    parser_classes = (JSONParser,)

    def get(self, request, id, format=None):
        try:
            item = Respuesta.objects.get(pk=id)
            serializer = RespuestaSerializer(item)
            return Response(serializer.data)
        except Respuesta.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Respuesta.objects.get(pk=id)
        except Respuesta.DoesNotExist:
            return Response(status=404)
        serializer = RespuestaSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Respuesta.objects.get(pk=id)
        except Respuesta.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class RespuestaAPIListView(APIView):
    
    renderer_classes = (JSONRenderer, )
    parser_classes = (JSONParser,)

    def get(self, request, format=None):
        items = Respuesta.objects.all()
        serializer = RespuestaSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RespuestaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class UsuarioAPIView(APIView):

    renderer_classes = (JSONRenderer, )
    parser_classes = (JSONParser,)

    def put(self, request, id, format=None):
        try:
            item = Usuario.objects.get(pk=id)
        except Usuario.DoesNotExist:
            return Response(status=404)
        serializer = UsuarioSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Usuario.objects.get(pk=id)
        except Usuario.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class UsuarioAPIListView(APIView):
    
    renderer_classes = (JSONRenderer, )
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class UsuarioAuthAPIListView(APIView):
    renderer_classes = (JSONRenderer,)
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        try:
            item = Usuario.objects.get(usuario=request.data['usuario'], password=request.data['password'])
            return Response({"auth": True})
        except Usuario.DoesNotExist:
            return Response({"auth": False})

        return Response(status=400)


class UsuarioAsignaturaAPIListView(APIView):
    
    renderer_classes = (JSONRenderer, )
    parser_classes = (JSONParser,)

    def get(self, request, id, format=None):
        items = UsuarioAsignatura.objects.filter(id_usuario=id)
        serializer = UsuarioAsignaturaSerializer(items, many=True)
        return Response(serializer.data)


class UsuarioTemaAPIListView(APIView):
    renderer_classes = (JSONRenderer,)
    parser_classes = (JSONParser,)

    def get(self, request, id, format=None):
        items = UsuarioTema.objects.filter(id_usuario=id)
        serializer = UsuarioTemaSerializer(items, many=True)
        return Response(serializer.data)


class UsuarioSubtemaAPIListView(APIView):
    renderer_classes = (JSONRenderer,)
    parser_classes = (JSONParser,)

    def get(self, request, id, format=None):
        items = UsuarioSubtema.objects.filter(id_usuario=id)
        serializer = UsuarioSubtemaSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, id, format=None):
        serializer = UsuarioSubtemaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            subtema = Subtema.objects.get(pk=request.data['id_subtema'])
            subtemas = Subtema.objects.filter(id_tema=subtema.id_tema.id_tema)
            u_tema = UsuarioTema.objects.get(id_tema=subtema.id_tema.id_tema, id_usuario= id)
            if not u_tema:
                porcentaje = (1/subtemas.count()) * 100
                u_tema = UsuarioTema(id_usuario=id, id_temas=subtema.id_tema.id_tema, porcentaje=porcentaje)
                u_tema.save()
                tema = Tema.objects.get(pk=u_tema.id_tema.id_tema)
                temas = Tema.objects.filter(id_asignatura=tema.id_asignatura.id_asignatura)
                u_asignatura = UsuarioAsignatura(id_usuario=id, id_asignatura=tema.id_asignatura.id_asignatura,
                                                 porcentaje=0.00)
                u_asignatura.save()
            else:
                id_subtemas = []
                correctos = 0
                for id_subtema in subtemas:
                    u_subtema = UsuarioSubtema.objects.get(id_subtema=id_subtema, completado=1)
                    if u_subtema:
                        correctos = correctos + 1
                porcentaje = (correctos.count()/subtemas.count()) * 100
                u_tema.porcentaje = porcentaje
                u_tema.save(update_fields=['porcentaje'])
                if porcentaje == 100.00:
                    tema = Tema.objects.get(pk=u_tema.id_tema.id_tema)
                    temas = Tema.objects.filter(id_asignatura=tema.id_asignatura.id_asignatura)
                    id_temas = []
                    completos = 0
                    for id_tema in temas:
                        u_tema = UsuarioTema.objects.get(id_tema=id_tema, porcentaje=100.00)
                        completos = completos + 1
                    u_asignatura = UsuarioAsignatura.objects.get(id_asignatura=tema.id_asignatura.id_asignatura,
                                                                 id_usuario=id)
                    porcentaje = (completos.count()/temas.count()) * 100
                    u_asignatura.porcentaje = porcentaje
                    u_asignatura.save(update_fields=['porcentaje'])

            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
