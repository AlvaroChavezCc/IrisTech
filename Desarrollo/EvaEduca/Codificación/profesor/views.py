import os
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from openai import OpenAI
from EvaSite import settings
from alumno.models import evaluacion
from profesor.forms import EditarTareaForm, LoginForm, ResetForm, crear_task
from .models import profesor
from administrador.models import curso, tareas
from .decorators import login_required
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
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    request.session.flush()  # Limpiar la sesión
    return redirect('login')

##ChatGPT

# Configuración del cliente OpenAI
client = OpenAI(api_key="sk-proj-R7BupP9cHyeKpCArExsjT3BlbkFJttLk5J0HF7Gpbav87B2m")

def read_docx(file_path):
    # Función para leer archivos .docx
    from docx import Document
    doc = Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

@login_required
def evaluate_tarea(request, tarea_id):
    tarea_obj = get_object_or_404(tareas, id=tarea_id)
    
    # Leer la rúbrica y la evaluación del alumno
    rubrica_path = tarea_obj.rubrica.path
    # Suponiendo que la rúbrica y la evaluación son archivos .docx
    rubrica_text = read_docx(rubrica_path)
    
    evaluaciones = evaluacion.objects.filter(id_tarea=tarea_obj)
    resultados = []

    for eval in evaluaciones:
        eval_path = eval.file.path
        eval_text = read_docx(eval_path)
        
        # Crear el prompt basado en la rúbrica y la evaluación del alumno
        prompt = f"Rúbrica:\n{rubrica_text}\n\nEvaluación del alumno:\n{eval_text}\n\nProporcione una evaluación basada en la rúbrica proporcionada."
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Evalúa el siguiente trabajo del alumno basado en la rúbrica dada."},
                {"role": "user", "content": prompt}
            ]
        )
        
        resultado = response['choices'][0]['message']['content']
        resultados.append({
            'alumno': eval.id_alumno.nombre,
            'resultado': resultado
        })

    return render(request, 'evaluar_tarea.html', {
        'tarea': tarea_obj,
        'resultados': resultados
    })


##ChatGPT

@login_required
def inicio(request):
    if 'profesor_id' in request.session:
        profesor_id = request.session['profesor_id']
        try:
            profesor_actual = profesor.objects.get(id=profesor_id)
            name = profesor_actual.nombre
        except profesor.DoesNotExist:
            print("Profesor no encontrado.")
            return redirect('login')
    else:
        print("Profesor ID no encontrado en sesión.")
        return redirect('login')

    return render(request, 'profesor.html', {
        'name': name
    })

@login_required
def tareas_curso(request, curso_id):
    curso_obj = get_object_or_404(curso, id=curso_id)
    tareas_curso = tareas.objects.filter(id_curso=curso_obj)
    evaluaciones_curso = evaluacion.objects.filter(id_curso=curso_obj)

    return render(request, 'tarea.html', {
        'curso': curso_obj,
        'tareas': tareas_curso,
        'evaluaciones': evaluaciones_curso
    })

@login_required
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

@login_required
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

@login_required
def cursos(request):
    # Obtener el profesor actualmente autenticado
    profesor_id = request.session.get('profesor_id')
    try:
        profesor_actual = profesor.objects.get(id=profesor_id)
    except profesor.DoesNotExist:
        messages.error(request, 'No se encontró al profesor')
        return redirect('login')
    
    # Obtener todos los cursos asignados a este profesor
    cursos_asignados = curso.objects.filter(id_profesor=profesor_actual)

    return render(request, 'cursos.html', {
        'profesor': profesor_actual,
        'cursos': cursos_asignados
    })

@login_required
def eliminar_tarea(request, tarea_id):
    tarea = get_object_or_404(tareas, id=tarea_id)
    curso_id = tarea.id_curso.id  # Guardar el curso_id antes de eliminar la tarea
    tarea.delete()
    messages.success(request, 'Tarea eliminada correctamente.')
    return redirect('tareas_curso', curso_id=curso_id)

@login_required
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