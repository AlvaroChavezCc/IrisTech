from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from administrador.models import tareas, curso
from .forms import LoginForm, EvaluacionForm
from .models import alumno, evaluacion

def login_alumno(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            contrasena = form.cleaned_data['contrasena']
            try:
                user = alumno.objects.get(usuario=usuario)
                if contrasena == user.contrasena:
                    request.session['alumno_id'] = user.id
                    request.session['alumno_nombre'] = user.nombre
                    return redirect('bienvenida_alumno')
                else:
                    messages.error(request, 'Contraseña incorrecta')
            except alumno.DoesNotExist:
                messages.error(request, 'Usuario no encontrado')
    else:
        form = LoginForm()
    return render(request, 'alumno/login.html', {'form': form})

def logout_alumno(request):
    request.session.flush()  # Limpiar la sesión
    return redirect('login_alumno')

def bienvenida(request):
    alumno_nombre = request.session.get('alumno_nombre', 'Alumno')
    mensaje_bienvenida = f"Bienvenido, {alumno_nombre}!"
    return render(request, 'alumno/Bienvenida.html', {'mensaje_bienvenida': mensaje_bienvenida})

def lista_tareas(request):
    tareas_alumno = evaluacion.objects.all()  # Asegúrate de usar el modelo evaluacion para obtener las tareas subidas
    return render(request, 'alumno/Lista_tareas.html', {'tareas': tareas_alumno})

def subir_respuesta(request):
    alumno_id = request.session.get('alumno_id')
    if not alumno_id:
        return redirect('login_alumno')

    alumno_instance = alumno.objects.get(id=alumno_id)
    curso_id = None
    show_errors = False

    if request.method == 'POST':
        if 'id_curso' in request.POST:
            curso_id = request.POST.get('id_curso')
            form = EvaluacionForm(request.POST, request.FILES, alumno=alumno_instance, curso_id=curso_id)
            if 'id_tarea' in request.POST and request.POST.get('id_tarea') != "":
                show_errors = True
        else:
            form = EvaluacionForm(request.POST, request.FILES, alumno=alumno_instance)
            show_errors = True

        if form.is_valid() and 'id_tarea' in request.POST:
            evaluacion_obj = form.save(commit=False)
            evaluacion_obj.id_alumno = alumno_instance
            evaluacion_obj.save()
            return redirect('bienvenida_alumno')
    else:
        form = EvaluacionForm(alumno=alumno_instance)

    return render(request, 'alumno/Subir_respuesta.html', {'form': form, 'curso_id': curso_id, 'show_errors': show_errors})

def eliminar_evaluacion(request, evaluacion_id):
    eval = get_object_or_404(evaluacion, id=evaluacion_id)
    eval.file.delete()  # Elimina el archivo físico del sistema de archivos
    eval.delete()  # Elimina el registro de la base de datos
    messages.success(request, 'La evaluación ha sido eliminada correctamente.')
    return redirect('lista_tareas')
