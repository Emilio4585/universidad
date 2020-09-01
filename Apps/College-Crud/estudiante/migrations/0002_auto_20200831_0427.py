# Generated by Django 3.0.3 on 2020-08-31 04:27

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('carrera', '0002_auto_20200830_2151'),
        ('estudiante', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estudiante',
            old_name='fecha_nacimiento',
            new_name='fechaNacimiento',
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='apellido_materno',
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='apellido_paterno',
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='codigo_carrera',
        ),
        migrations.AddField(
            model_name='estudiante',
            name='apellidoMaterno',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='apellidoPaterno',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='codigoCarrera',
            field=models.ForeignKey(blank=True, default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='carrera.Carrera'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='dni',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='nombres',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='sexo',
            field=models.CharField(blank=True, choices=[('F', 'Femenino'), ('M', 'Masculino')], default='F', max_length=20),
        ),
    ]