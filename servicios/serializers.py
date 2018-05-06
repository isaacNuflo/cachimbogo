from rest_framework.serializers import ModelSerializer, SerializerMethodField
from servicios.models import Asignatura, Dificultad, Informacion, Tema, Subtema, TipoPregunta, Pregunta, Respuesta, Usuario, UsuarioHasAsignatura


class AsignaturaSerializer(ModelSerializer):

    class Meta:
        model = Asignatura
        fields = '__all__'


class DificultadSerializer(ModelSerializer):

    class Meta:
        model = Dificultad
        fields = '__all__'


class TemaAsignaturaSerializer(ModelSerializer):
    
    class Meta:
        model = Tema
        fields = '__all__'


class SubtemaTemaSerializer(ModelSerializer):
    
    class Meta:
        model = Subtema
        fields = '__all__'        


class TemaSerializer(ModelSerializer):
    asignatura = SerializerMethodField()

    def get_asignatura(self,tema):
      asignatura = AsignaturaSerializer(tema.asignatura,many=False,read_only=True)
      return asignatura.data

    class Meta:
        model = Tema
        fields = '__all__'


class SubtemaSerializer(ModelSerializer):
    tema = SerializerMethodField()

    def get_tema(self,subtema):
        tema = TemaSerializer(subtema.tema,many=False,read_only=True)
        return tema.data

    class Meta:
        model = Subtema
        fields = '__all__'


class TipoPreguntaSerializer(ModelSerializer):

    class Meta:
        model = TipoPregunta
        fields = '__all__'


class PreguntaTSerializer(ModelSerializer):
    
    class Meta:
        model = Pregunta
        fields = '__all__'


class PreguntaSerializer(ModelSerializer):
    dificultad = SerializerMethodField()
    subtema = SerializerMethodField()
    tipo_pregunta = SerializerMethodField()
    
    def get_tipo_pregunta(self,pregunta):
        tipo_pregunta = TipoPreguntaSerializer(pregunta.tipo_pregunta_id_tipopregunta,many=False,read_only=True)
        return tipo_pregunta.data

    def get_informacion(self,pregunta):
        informacion = InformacionSerializer(pregunta.informacion_id_informacion,many=False,read_only=True)
        return informacion.data

    def get_subtema(self,pregunta):
        subtema = SubtemaSerializer(pregunta.subtema_id_subtema,many=False,read_only=True)
        return subtema.data

    def get_dificultad(self,pregunta):
        dificultad = DificultadSerializer(pregunta.dificultad_id_dificultad,many=False, read_only=True)
        return dificultad.data
 
    class Meta:
        model = Pregunta
        fields = '__all__'


class RespuestaSerializer(ModelSerializer):

    class Meta:
        model = Respuesta
        fields = '__all__'


class UsuarioSerializer(ModelSerializer):

    class Meta:
        model = Usuario
        fields = '__all__'


class UsuarioHasAsignaturaSerializer(ModelSerializer):

    class Meta:
        model = UsuarioHasAsignatura
        fields = '__all__'
