# Generated by Django 3.0.3 on 2020-08-31 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matricula', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matricula',
            name='fecha_matricula',
            field=models.DateField(),
        ),
    ]
