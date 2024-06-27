from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import tareas
from django.contrib.auth import authenticate, login, logout
from .forms import SubirRespuestaForm, LoginForm
from .models import Examen, alumno


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
                    return redirect('cargar-respuesta')
                else:
                    messages.error(request, 'Contraseña incorrecta')
            except alumno.DoesNotExist:
                messages.error(request, 'Usuario no encontrado')
    else:
        form = LoginForm()
    return render(request, 'alumno/login.html', {'form': form})



def logout_alumno(request):
    request.session.flush()  # Limpiar la sesión
    return redirect('alumno_login')


#@login_required
def descargar_examen(request):
    examen_id = request.GET.get('examen_id')
    examen = get_object_or_404(Examen, pk=examen_id)
    
    # Suponiendo que `archivo` es el campo que contiene el archivo que deseas descargar
    if examen.archivo:
        file_path = examen.archivo.path  # Obtén la ruta del archivo en el sistema de archivos
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = 'attachment; filename=' + examen.archivo.name
            return response
    else:
        # Manejo si el examen no tiene archivo adjunto
        return HttpResponse('El examen seleccionado no tiene archivo adjunto.')


#@login_required
def cargar_respuesta(request, tareas_id):
    # Obtener la tarea según el ID proporcionado en la URL
    tarea = get_object_or_404(tareas, id=tareas_id)
    
    if request.method == 'POST':
        form = SubirRespuestaForm(request.POST, request.FILES)
        if form.is_valid():
            respuesta = form.save(commit=False)
            respuesta.alumno = request.user  # Asignar el usuario actual como alumno
            respuesta.tareas = tarea  # Asignar la tarea seleccionada
            respuesta.save()
            messages.success(request, 'Respuesta cargada exitosamente.')
            return redirect('cargar_respuesta', tareas_id=tareas_id) 
    else:
        form = SubirRespuestaForm()
    
    return render(request, 'alumno/cargar_respuesta.html', {'form': form, 'tarea': tarea})



#@login_required  # Asegura que solo usuarios autenticados puedan acceder a esta vista
def inicio(request):
    if 'alumno_id' in request.session:
        alumno_id = request.session['alumno_id']
        try:
            profesor_actual = alumno.objects.get(id=alumno_id)
            name = profesor_actual.nombre
        except alumno.DoesNotExist:
            print("Alumno no encontrado.")
            return redirect('login')
    else:
        print("Alumno ID no encontrado en sesión.")
        return redirect('login')

    return render(request, 'alumno/login.html', {
        'name': name
    })

  