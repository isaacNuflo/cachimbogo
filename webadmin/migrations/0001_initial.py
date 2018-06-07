# Generated by Django 2.0.6 on 2018-06-07 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id_asignatura', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'asignatura',
            },
        ),
        migrations.CreateModel(
            name='Dificultad',
            fields=[
                ('id_dificultad', models.AutoField(primary_key=True, serialize=False)),
                ('nivel', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'dificultad',
            },
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id_pregunta', models.AutoField(primary_key=True, serialize=False)),
                ('enunciado', models.CharField(max_length=1000)),
                ('clave1', models.CharField(max_length=200)),
                ('clave2', models.CharField(max_length=200)),
                ('clave3', models.CharField(max_length=200)),
                ('clave4', models.CharField(max_length=200)),
                ('clave5', models.CharField(max_length=200)),
                ('estado', models.IntegerField(blank=True, null=True)),
                ('correcta_num', models.SmallIntegerField(blank=True, null=True)),
                ('informacion', models.CharField(blank=True, max_length=800, null=True)),
                ('id_dificultad', models.ForeignKey(db_column='id_dificultad', on_delete=django.db.models.deletion.DO_NOTHING, to='webadmin.Dificultad')),
            ],
            options={
                'db_table': 'pregunta',
            },
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acertada', models.IntegerField(blank=True, null=True)),
                ('id_pregunta', models.ForeignKey(db_column='id_pregunta', on_delete=django.db.models.deletion.DO_NOTHING, to='webadmin.Pregunta')),
            ],
            options={
                'db_table': 'respuesta',
            },
        ),
        migrations.CreateModel(
            name='Subtema',
            fields=[
                ('id_subtema', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'subtema',
            },
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id_tema', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('id_asignatura', models.ForeignKey(db_column='id_asignatura', on_delete=django.db.models.deletion.DO_NOTHING, to='webadmin.Asignatura')),
            ],
            options={
                'db_table': 'tema',
            },
        ),
        migrations.CreateModel(
            name='TipoPregunta',
            fields=[
                ('id_tipopregunta', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'tipo_pregunta',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('usuario', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('nombres', models.CharField(blank=True, max_length=80, null=True)),
                ('apellidos', models.CharField(blank=True, max_length=80, null=True)),
                ('correo', models.CharField(blank=True, max_length=30, null=True)),
                ('monedas', models.SmallIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'usuario',
            },
        ),
        migrations.CreateModel(
            name='UsuarioAsignatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porcentaje', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('id_asignatura', models.ForeignKey(db_column='id_asignatura', on_delete=django.db.models.deletion.DO_NOTHING, to='webadmin.Asignatura')),
                ('id_usuario', models.ForeignKey(db_column='id_usuario', on_delete=django.db.models.deletion.DO_NOTHING, to='webadmin.Usuario')),
            ],
            options={
                'db_table': 'usuario_asignatura',
            },
        ),
        migrations.CreateModel(
            name='UsuarioSubtema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porcentaje', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('id_subtema', models.ForeignKey(db_column='id_subtema', on_delete=django.db.models.deletion.DO_NOTHING, to='webadmin.Subtema')),
                ('id_usuario', models.ForeignKey(db_column='id_usuario', on_delete=django.db.models.deletion.DO_NOTHING, to='webadmin.Usuario')),
            ],
            options={
                'db_table': 'usuario_subtema',
            },
        ),
        migrations.CreateModel(
            name='UsuarioTema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porcentaje', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('id_tema', models.ForeignKey(db_column='id_tema', on_delete=django.db.models.deletion.DO_NOTHING, to='webadmin.Tema')),
                ('id_usuario', models.ForeignKey(db_column='id_usuario', on_delete=django.db.models.deletion.DO_NOTHING, to='webadmin.Usuario')),
            ],
            options={
                'db_table': 'usuario_tema',
            },
        ),
        migrations.AddField(
            model_name='subtema',
            name='id_tema',
            field=models.ForeignKey(db_column='id_tema', on_delete=django.db.models.deletion.DO_NOTHING, to='webadmin.Tema'),
        ),
        migrations.AddField(
            model_name='respuesta',
            name='id_usuario',
            field=models.ForeignKey(db_column='id_usuario', on_delete=django.db.models.deletion.DO_NOTHING, to='webadmin.Usuario'),
        ),
        migrations.AddField(
            model_name='pregunta',
            name='id_subtema',
            field=models.ForeignKey(db_column='id_subtema', on_delete=django.db.models.deletion.DO_NOTHING, to='webadmin.Subtema'),
        ),
        migrations.AddField(
            model_name='pregunta',
            name='id_tipopregunta',
            field=models.ForeignKey(db_column='id_tipopregunta', on_delete=django.db.models.deletion.DO_NOTHING, to='webadmin.TipoPregunta'),
        ),
        migrations.AlterUniqueTogether(
            name='usuariotema',
            unique_together={('id_usuario', 'id_tema')},
        ),
        migrations.AlterUniqueTogether(
            name='usuariosubtema',
            unique_together={('id_usuario', 'id_subtema')},
        ),
        migrations.AlterUniqueTogether(
            name='usuarioasignatura',
            unique_together={('id_usuario', 'id_asignatura')},
        ),
        migrations.AlterUniqueTogether(
            name='respuesta',
            unique_together={('id_usuario', 'id_pregunta')},
        ),
    ]
