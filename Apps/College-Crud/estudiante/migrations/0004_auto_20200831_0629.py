# Generated by Django 3.0.3 on 2020-08-31 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0003_auto_20200831_0628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='vigencia',
            field=models.BooleanField(default=True),
        ),
    ]