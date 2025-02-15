# Generated by Django 5.0.6 on 2024-06-26 05:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0003_alter_tareas_archivo_alter_tareas_rubrica'),
        ('profesor', '0002_alter_profesor_usuario'),
        ('superadmin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='id_inst_ed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superadmin.institucion'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='id_profesor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profesor.profesor'),
        ),
    ]
