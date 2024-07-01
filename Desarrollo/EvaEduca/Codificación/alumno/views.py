from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from administrador.models import tareas
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
    mensaje_bienvenida = "Bienvenido!"

    return render(request, 'alumno/Bienvenida.html', {'mensaje_bienvenida': mensaje_bienvenida})

def lista_tareas(request):
    tareas_alumno = tareas.objects.all()  
    print(tareas_alumno) 
    return render(request, 'alumno/Lista_tareas.html', {'tareas': tareas_alumno})



def subir_respuesta(request):
    if request.method == 'POST':
        form = EvaluacionForm(request.POST, request.FILES)
        if form.is_valid():
            # Obtener el ID del alumno 
            id_alumno_id =  request.session['alumno_id']  
            
            # Guardar la evaluación en la base de datos asignando id_alumno_id
            evaluacion_obj = form.save(commit=False)
            evaluacion_obj.id_alumno_id = id_alumno_id
            evaluacion_obj.save()

            return redirect('bienvenida_alumno')
    else:
        form = EvaluacionForm()

        return render(request, 'alumno/Subir_respuesta.html', {'form': form})








  