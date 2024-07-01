from django.shortcuts import render, redirect
from django.contrib import messages
from administrador.models import tareas, curso
from .forms import LoginForm, EvaluacionForm
from .models import alumno

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
    tareas_alumno = tareas.objects.all()  
    print(tareas_alumno) 
    return render(request, 'alumno/Lista_tareas.html', {'tareas': tareas_alumno})

def subir_respuesta(request):
    alumno_id = request.session.get('alumno_id')
    if not alumno_id:
        return redirect('login_alumno')
    
    alumno_instance = alumno.objects.get(id=alumno_id)
    
    if request.method == 'POST':
        form = EvaluacionForm(request.POST, request.FILES, alumno=alumno_instance)
        if form.is_valid():
            evaluacion_obj = form.save(commit=False)
            evaluacion_obj.id_alumno = alumno_instance
            evaluacion_obj.save()
            return redirect('bienvenida_alumno')
    else:
        form = EvaluacionForm(alumno=alumno_instance)
    
    return render(request, 'alumno/Subir_respuesta.html', {'form': form})
