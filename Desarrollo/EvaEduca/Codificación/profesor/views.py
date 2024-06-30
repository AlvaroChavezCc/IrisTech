import os
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from openai import OpenAI
from EvaSite import settings
from alumno.models import evaluacion, reclamo
from profesor.forms import EditarTareaForm, EvaluarManualmenteForm, JustificarNotaForm, LoginForm, ModificarNotaForm, ResetForm, crear_task
from .models import profesor
from administrador.models import curso, tareas
from .decorators import profesor_login_required
from docx import Document
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            contrasena = form.cleaned_data['contrasena']
            try:
                user = profesor.objects.get(usuario=usuario)
                if contrasena == user.contrasena:
                    request.session['profesor_id'] = user.id
                    return redirect('profesor')
                else:
                    messages.error(request, 'Contraseña incorrecta')
            except profesor.DoesNotExist:
                messages.error(request, 'Usuario no encontrado')
    else:
        form = LoginForm()
    return render(request, 'login_p.html', {'form': form})

def logout_view(request):
    request.session.flush()  # Limpiar la sesión
    return redirect('login_p')

##ChatGPT

# Configuración del cliente OpenAI
client = OpenAI(api_key="sk-proj-l1jhmQnVBraVxTpb83s7T3BlbkFJq2MorTJZCtPEqaS18uFI")

def read_docx(file_path):
    # Función para leer archivos .docx
    doc = Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

@profesor_login_required
def evaluate_tarea(request, tarea_id):
    tarea_obj = get_object_or_404(tareas, id=tarea_id)
    
    # Leer la rúbrica y la evaluación del alumno
    rubrica_path = tarea_obj.rubrica.path
    rubrica_text = read_docx(rubrica_path)
    
    # Filtrar solo las evaluaciones que no han sido calificadas
    evaluaciones = evaluacion.objects.filter(id_tarea=tarea_obj, nota__isnull=True)
    resultados = []

    for eval in evaluaciones:
        eval_path = eval.file.path
        eval_text = read_docx(eval_path)
        
        # Crear el prompt basado en la rúbrica y la evaluación del alumno
        prompt = f"Rúbrica:\n{rubrica_text}\n\nEvaluación del alumno:\n{eval_text}\n\nProporcione una evaluación basada en la rúbrica proporcionada e incluya una línea clara con la nota en el formato 'Nota: X' donde X es un número del 0 al 20."
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Evalúa el siguiente trabajo del alumno basado en la rúbrica dada y proporciona una nota del 0 al 20."},
                {"role": "user", "content": prompt}
            ]
        )
        
        if response and response.choices:
            resultado = response.choices[0].message.content
            
            # Aquí asumimos que la nota se encuentra en una línea que dice "Nota: X" en el resultado
            nota_line = next((line for line in resultado.split('\n') if "Nota:" in line), None)
            nota = None
            if nota_line:
                try:
                    nota = float(nota_line.split(':')[1].strip())
                except ValueError:
                    pass
            
            # Almacenar la nota y la respuesta en el modelo evaluacion
            eval.nota = nota
            eval.respuesta = resultado
            eval.save()

            resultados.append({
                'alumno': eval.id_alumno.nombre,
                'resultado': resultado,
                'nota': nota
            })
        else:
            resultados.append({
                'alumno': eval.id_alumno.nombre,
                'resultado': "No se pudo obtener una respuesta en este momento.",
                'nota': None
            })

    return redirect('visualizar_evaluaciones', tarea_id=tarea_id)

##ChatGPT

@profesor_login_required
def inicio(request):
    if 'profesor_id' in request.session:
        profesor_id = request.session['profesor_id']
        try:
            profesor_actual = profesor.objects.get(id=profesor_id)
            name = profesor_actual.nombre
        except profesor.DoesNotExist:
            print("Profesor no encontrado.")
            return redirect('login_p')
    else:
        print("Profesor ID no encontrado en sesión.")
        return redirect('login_p')

    return render(request, 'profesor.html', {
        'name': name
    })

@profesor_login_required
def tareas_curso(request, curso_id):
    curso_obj = get_object_or_404(curso, id=curso_id)
    tareas_curso = tareas.objects.filter(id_curso=curso_obj)
    evaluaciones_curso = evaluacion.objects.filter(id_curso=curso_obj)

    return render(request, 'tarea.html', {
        'curso': curso_obj,
        'tareas': tareas_curso,
        'evaluaciones': evaluaciones_curso
    })

@profesor_login_required
def crear_tarea(request, curso_id):
    curso_obj = get_object_or_404(curso, id=curso_id)
    
    if request.method == 'GET':
        form = crear_task()
        return render(request, 'crear_tarea.html', {
            'form': form,
            'curso': curso_obj
        })
    else:
        form = crear_task(request.POST, request.FILES)
        if form.is_valid():
            tarea = tareas.objects.create(
                id_curso=curso_obj,
                tema=form.cleaned_data['tema'],
                descripcion=form.cleaned_data['descripcion'],
                rubrica=form.cleaned_data.get('rubrica'),
                archivo=form.cleaned_data.get('archivo')
            )
            return redirect('tareas_curso', curso_id=curso_obj.id)
        return render(request, 'crear_tarea.html', {
            'form': form,
            'curso': curso_obj
        })
    
@profesor_login_required
def visualizar_evaluaciones(request, tarea_id):
    tarea_obj = get_object_or_404(tareas, id=tarea_id)
    evaluaciones = evaluacion.objects.filter(id_tarea=tarea_obj)
    # Verificar si hay evaluaciones sin calificar
    hay_evaluaciones_pendientes = evaluaciones.filter(nota__isnull=True).exists()
    return render(request, 'visualizar_evaluaciones.html', {'tarea': tarea_obj, 'evaluaciones': evaluaciones, 'hay_evaluaciones_pendientes': hay_evaluaciones_pendientes})

@profesor_login_required
def resetear(request):
    profesor_id = request.session.get('profesor_id')
    profesor_obj = get_object_or_404(profesor, id=profesor_id)
    
    if request.method == 'POST':
        form = ResetForm(request.POST, instance=profesor_obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario y contraseña actualizados correctamente.')
            return redirect('reset')
    else:
        form = ResetForm(instance=profesor_obj)
    
    return render(request, 'resetear.html', {
        'form': form
    })

@profesor_login_required
def cursos(request):
    # Obtener el profesor actualmente autenticado
    profesor_id = request.session.get('profesor_id')
    try:
        profesor_actual = profesor.objects.get(id=profesor_id)
    except profesor.DoesNotExist:
        messages.error(request, 'No se encontró al profesor')
        return redirect('login_p')
    
    # Obtener todos los cursos asignados a este profesor
    cursos_asignados = curso.objects.filter(id_profesor=profesor_actual)

    return render(request, 'cursos.html', {
        'profesor': profesor_actual,
        'cursos': cursos_asignados
    })

@profesor_login_required
def eliminar_tarea(request, tarea_id):
    tarea = get_object_or_404(tareas, id=tarea_id)
    curso_id = tarea.id_curso.id  # Guardar el curso_id antes de eliminar la tarea
    tarea.delete()
    messages.success(request, 'Tarea eliminada correctamente.')
    return redirect('tareas_curso', curso_id=curso_id)

@profesor_login_required
def editar_tarea(request, tarea_id):
    tarea = get_object_or_404(tareas, id=tarea_id)
    if request.method == 'POST':
        form = EditarTareaForm(request.POST, request.FILES, instance=tarea)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarea actualizada correctamente.')
            return redirect('tareas_curso', curso_id=tarea.id_curso.id)
    else:
        form = EditarTareaForm(instance=tarea)
    
    return render(request, 'editar_tarea.html', {
        'form': form,
        'tarea': tarea
    })

@profesor_login_required
def ver_respuesta(request, evaluacion_id):
    evaluacion_obj = get_object_or_404(evaluacion, id=evaluacion_id)
    return render(request, 'ver_respuesta.html', {
        'evaluacion': evaluacion_obj
    })

@profesor_login_required
def evaluar_manualmente(request, evaluacion_id):
    evaluacion_obj = get_object_or_404(evaluacion, id=evaluacion_id)
    
    if request.method == 'POST':
        form = EvaluarManualmenteForm(request.POST)
        if form.is_valid():
            evaluacion_obj.nota = form.cleaned_data['nota']
            evaluacion_obj.respuesta = form.cleaned_data['respuesta']
            evaluacion_obj.save()
            messages.success(request, 'Evaluación manual guardada correctamente.')
            return redirect('visualizar_evaluaciones', tarea_id=evaluacion_obj.id_tarea.id)
    else:
        form = EvaluarManualmenteForm()
    
    return render(request, 'eval_man.html', {
        'form': form,
        'evaluacion': evaluacion_obj
    })

@profesor_login_required
def lista_reclamos(request):
    reclamos = reclamo.objects.filter(estado=True).select_related('id_alumno', 'id_evaluacion__id_curso', 'id_evaluacion__id_tarea')
    context = {
        'reclamos': reclamos
    }
    return render(request, 'lista_reclamos.html', context)

@profesor_login_required
def atender_reclamo(request, reclamo_id):
    reclamo_obj = get_object_or_404(reclamo, id=reclamo_id)
    context = {
        'reclamo': reclamo_obj
    }
    return render(request, 'atender_reclamo.html', context)

@profesor_login_required
def justificar_nota(request, reclamo_id):
    reclamo_obj = get_object_or_404(reclamo, id=reclamo_id)
    
    if request.method == 'POST':
        form = JustificarNotaForm(request.POST)
        if form.is_valid():
            reclamo_obj.respuesta = form.cleaned_data['respuesta']
            reclamo_obj.estado = False
            reclamo_obj.save()
            return redirect('lista_reclamos')
    else:
        form = JustificarNotaForm()
    
    context = {
        'form': form,
        'reclamo': reclamo_obj
    }
    return render(request, 'justificar_nota.html', context)

@profesor_login_required
def modificar_nota(request, reclamo_id):
    reclamo_obj = get_object_or_404(reclamo, id=reclamo_id)
    evaluacion_obj = reclamo_obj.id_evaluacion
    
    if request.method == 'POST':
        form = ModificarNotaForm(request.POST)
        if form.is_valid():
            reclamo_obj.respuesta = form.cleaned_data['respuesta_reclamo']
            reclamo_obj.estado = False
            reclamo_obj.save()
            
            evaluacion_obj.nota = form.cleaned_data['nota']
            evaluacion_obj.respuesta = form.cleaned_data['respuesta_evaluacion']
            evaluacion_obj.save()
            
            return redirect('lista_reclamos')
    else:
        form = ModificarNotaForm(initial={
            'nota': evaluacion_obj.nota,
            'respuesta_evaluacion': evaluacion_obj.respuesta,
            'respuesta_reclamo': reclamo_obj.respuesta,
        })
    
    context = {
        'form': form,
        'reclamo': reclamo_obj
    }
    return render(request, 'modificar_nota.html', context)