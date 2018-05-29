from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from servicios.serializers import PreguntaTSerializer, AsignaturaSerializer, DificultadSerializer, TemaSerializer,SubtemaTemaSerializer,TemaAsignaturaSerializer, SubtemaSerializer, TipoPreguntaSerializer, PreguntaSerializer, RespuestaSerializer, UsuarioSerializer, UsuarioHasAsignaturaSerializer
from servicios.models import Asignatura, Dificultad, Tema, Subtema, TipoPregunta, Pregunta, Respuesta, Usuario, UsuarioAsignatura
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
        items = Asignatura.objects.all()
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

    def get(self, request, id , format=None):
        items = Pregunta.objects.filter(id_subtema__id_subtema=id)
        lists = []
        response = {}
        first = items[0].id_pregunta
        last = items.last().id_pregunta
        i = 1
        while i <= 7:
            rand = random.randint(first, last)
            if not lists:
                lists.append(rand)
                response[str(i)] = self.get_answer(rand)
                i = i + 1
            elif rand not in lists:
                lists.append(rand)
                response[str(i)] = self.get_answer(rand)
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

    def get(self, request, id, format=None):
        try:
            item = Usuario.objects.get(pk=id)
            serializer = UsuarioSerializer(item)
            return Response(serializer.data)
        except Usuario.DoesNotExist:
            return Response(status=404)

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

    def get(self, request, format=None):
        items = Usuario.objects.all()
        serializer = UsuarioSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class UsuarioAsignaturaAPIView(APIView):
    
    renderer_classes = (JSONRenderer, )
    parser_classes = (JSONParser,)

    def get(self, request, id, format=None):
        try:
            item = UsuarioAsignatura.objects.get(pk=id)
            serializer = UsuarioHasAsignaturaSerializer(item)
            return Response(serializer.data)
        except UsuarioAsignatura.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = UsuarioAsignatura.objects.get(pk=id)
        except UsuarioAsignatura.DoesNotExist:
            return Response(status=404)
        serializer = UsuarioHasAsignaturaSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = UsuarioAsignatura.objects.get(pk=id)
        except UsuarioAsignatura.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class UsuarioAsignaturaAPIListView(APIView):
    
    renderer_classes = (JSONRenderer, )
    parser_classes = (JSONParser,)

    def get(self, request, format=None):
        items = UsuarioAsignatura.objects.all()
        serializer = UsuarioHasAsignaturaSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UsuarioHasAsignaturaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
