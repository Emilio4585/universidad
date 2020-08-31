# Generated by Django 3.0.3 on 2020-08-28 18:45

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('codigo', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100)),
                ('creditos', models.IntegerField()),
                ('docente', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
