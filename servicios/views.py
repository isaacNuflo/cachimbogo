from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from servicios.serializers import AsignaturaSerializer, DificultadSerializer, InformacionSerializer, TemaSerializer, SubtemaSerializer, TipoPreguntaSerializer, PreguntaSerializer, RespuestaSerializer, UsuarioSerializer, UsuarioHasAsignaturaSerializer
from servicios.models import Asignatura, Dificultad, Informacion, Tema, Subtema, TipoPregunta, Pregunta, Respuesta, Usuario, UsuarioHasAsignatura


class AsignaturaAPIView(APIView):

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

    def get(self, request, format=None):
        items = Asignatura.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = AsignaturaSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = AsignaturaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class DificultadAPIView(APIView):

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

    def get(self, request, format=None):
        items = Dificultad.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = DificultadSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = DificultadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class InformacionAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Informacion.objects.get(pk=id)
            serializer = InformacionSerializer(item)
            return Response(serializer.data)
        except Informacion.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Informacion.objects.get(pk=id)
        except Informacion.DoesNotExist:
            return Response(status=404)
        serializer = InformacionSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Informacion.objects.get(pk=id)
        except Informacion.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class InformacionAPIListView(APIView):

    def get(self, request, format=None):
        items = Informacion.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = InformacionSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = InformacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class TemaAPIView(APIView):

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

    def get(self, request, format=None):
        items = Tema.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = TemaSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = TemaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class SubtemaAPIView(APIView):

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

    def get(self, request, format=None):
        items = Subtema.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = SubtemaSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = SubtemaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class TipoPreguntaAPIView(APIView):

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

    def get(self, request, format=None):
        items = TipoPregunta.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = TipoPreguntaSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = TipoPreguntaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class PreguntaAPIView(APIView):

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


class PreguntaAPIListView(APIView):

    def get(self, request, format=None):
        items = Pregunta.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = PreguntaSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = PreguntaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class RespuestaAPIView(APIView):

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

    def get(self, request, format=None):
        items = Respuesta.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = RespuestaSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = RespuestaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class UsuarioAPIView(APIView):

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

    def get(self, request, format=None):
        items = Usuario.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = UsuarioSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class UsuarioHasAsignaturaAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = UsuarioHasAsignatura.objects.get(pk=id)
            serializer = UsuarioHasAsignaturaSerializer(item)
            return Response(serializer.data)
        except UsuarioHasAsignatura.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = UsuarioHasAsignatura.objects.get(pk=id)
        except UsuarioHasAsignatura.DoesNotExist:
            return Response(status=404)
        serializer = UsuarioHasAsignaturaSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = UsuarioHasAsignatura.objects.get(pk=id)
        except UsuarioHasAsignatura.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class UsuarioHasAsignaturaAPIListView(APIView):

    def get(self, request, format=None):
        items = UsuarioHasAsignatura.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = UsuarioHasAsignaturaSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = UsuarioHasAsignaturaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
