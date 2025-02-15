# Generated by Django 5.0.6 on 2024-06-30 12:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumno', '0005_evaluacion_nota_evaluacion_respuesta'),
    ]

    operations = [
        migrations.CreateModel(
            name='reclamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('respuesta', models.TextField(blank=True, null=True)),
                ('estado', models.BooleanField(default=True)),
                ('id_alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumno.alumno')),
                ('id_evaluacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumno.evaluacion')),
            ],
        ),
    ]
