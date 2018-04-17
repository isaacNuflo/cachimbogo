# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Asignatura(models.Model):
    id_asignatura = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    completado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ASIGNATURA'


class Dificultad(models.Model):
    id_dificultad = models.AutoField(primary_key=True)
    nivel = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'DIFICULTAD'


class Informacion(models.Model):
    id_informacion = models.AutoField(primary_key=True)
    informacion = models.CharField(max_length=800, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'INFORMACION'


class Tema(models.Model):
    id_tema = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    completado = models.IntegerField(blank=True, null=True)
    asignatura_id_asignatura = models.ForeignKey(Asignatura, models.DO_NOTHING, db_column='ASIGNATURA_id_asignatura')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEMA'


class Subtema(models.Model):
    id_subtema = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    completado = models.IntegerField(blank=True, null=True)
    tema_id_tema = models.ForeignKey(Tema, models.DO_NOTHING, db_column='TEMA_id_tema')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SUBTEMA'


class TipoPregunta(models.Model):
    id_tipopregunta = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'TIPO_PREGUNTA'


class Pregunta(models.Model):
    id_pregunta = models.AutoField(primary_key=True)
    enunciado = models.CharField(max_length=1000)
    clave1 = models.CharField(max_length=200)
    clave2 = models.CharField(max_length=200)
    clave3 = models.CharField(max_length=200)
    clave4 = models.CharField(max_length=200)
    clave5 = models.CharField(max_length=200)
    correcta = models.CharField(max_length=200)
    estado = models.IntegerField(blank=True, null=True)
    informacion_id_informacion = models.ForeignKey(Informacion, models.DO_NOTHING, db_column='INFORMACION_id_informacion', blank=True, null=True)  # Field name made lowercase.
    subtema_id_subtema = models.ForeignKey(Subtema, models.DO_NOTHING, db_column='SUBTEMA_id_subtema')  # Field name made lowercase.
    tipo_pregunta_id_tipopregunta = models.ForeignKey(TipoPregunta, models.DO_NOTHING, db_column='TIPO_PREGUNTA_id_tipopregunta')  # Field name made lowercase.
    dificultad_id_dificultad = models.ForeignKey(Dificultad, models.DO_NOTHING, db_column='DIFICULTAD_id_dificultad')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PREGUNTA'


class Respuesta(models.Model):
    id_respuesta = models.AutoField(primary_key=True)
    acertada = models.IntegerField(blank=True, null=True)
    pregunta_id_pregunta = models.ForeignKey(Pregunta, models.DO_NOTHING, db_column='PREGUNTA_id_pregunta')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RESPUESTA'


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    nombres = models.CharField(max_length=80, blank=True, null=True)
    apellidos = models.CharField(max_length=80, blank=True, null=True)
    correo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'USUARIO'


class UsuarioHasAsignatura(models.Model):
    usuario_id_usuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='USUARIO_id_usuario')  # Field name made lowercase.
    asignatura_id_asignatura = models.ForeignKey(Asignatura, models.DO_NOTHING, db_column='ASIGNATURA_id_asignatura')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USUARIO_has_ASIGNATURA'
        unique_together = (('usuario_id_usuario', 'asignatura_id_asignatura'),)
