from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .decorators import login_required
from .models import administrador, curso
from profesor.models import profesor
from alumno.models import alumno
from .forms import CursoForm, ProfesorForm, AlumnoForm, LoginForm

# Vista de Redirección
@login_required
def home(request):
    return redirect('curso_list')

# Vistas de Login
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            contrasena = form.cleaned_data['contrasena']
            try:
                admin = administrador.objects.get(usuario=usuario)
                if contrasena == admin.contrasena:
                    request.session['administrador_id'] = admin.id
                    return redirect('curso_list')
                else:
                    messages.error(request, 'Contraseña incorrecta')
            except administrador.DoesNotExist:
                messages.error(request, 'Usuario no encontrado')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

# Vistas de Profesor
@login_required
def profesor_list(request):
    profesores = profesor.objects.all()
    return render(request, 'profesor_list.html', {'profesores': profesores})

@login_required
def profesor_create(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profesor_list')
    else:
        form = ProfesorForm()
    return render(request, 'profesor_form.html', {'form': form})

@login_required
def profesor_update(request, pk):
    profesor_obj = get_object_or_404(profesor, pk=pk)
    if request.method == 'POST':
        form = ProfesorForm(request.POST, instance=profesor_obj)
        if form.is_valid():
            form.save()
            return redirect('profesor_list')
    else:
        form = ProfesorForm(instance=profesor_obj)
    return render(request, 'profesor_form.html', {'form': form})

@login_required
def profesor_delete(request, pk):
    profesor_obj = get_object_or_404(profesor, pk=pk)
    if request.method == 'POST':
        profesor_obj.delete()
        return redirect('profesor_list')
    return render(request, 'profesor_confirm_delete.html', {'profesor': profesor_obj})

# Vistas de Curso
@login_required
def curso_list(request):
    cursos = curso.objects.all()
    return render(request, 'curso_list.html', {'cursos': cursos})

@login_required
def curso_create(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('curso_list')
    else:
        form = CursoForm()
    return render(request, 'curso_form.html', {'form': form})

@login_required
def curso_update(request, pk):
    curso_obj = get_object_or_404(curso, pk=pk)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso_obj)
        if form.is_valid():
            form.save()
            return redirect('curso_list')
    else:
        form = CursoForm(instance=curso_obj)
    return render(request, 'curso_form.html', {'form': form})

@login_required
def curso_delete(request, pk):
    curso_obj = get_object_or_404(curso, pk=pk)
    if request.method == 'POST':
        curso_obj.delete()
        return redirect('curso_list')
    return render(request, 'curso_confirm_delete.html', {'curso': curso_obj})

# Vistas de Alumno
@login_required
def alumno_list(request):
    alumnos = alumno.objects.all()
    return render(request, 'alumno_list.html', {'alumnos': alumnos})

@login_required
def alumno_create(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alumno_list')
    else:
        form = AlumnoForm()
    return render(request, 'alumno_form.html', {'form': form})

@login_required
def alumno_update(request, pk):
    alumno_obj = get_object_or_404(alumno, pk=pk)
    if request.method == 'POST':
        form = AlumnoForm(request.POST, instance=alumno_obj)
        if form.is_valid():
            form.save()
            return redirect('alumno_list')
    else:
        form = AlumnoForm(instance=alumno_obj)
    return render(request, 'alumno_form.html', {'form': form})

@login_required
def alumno_delete(request, pk):
    alumno_obj = get_object_or_404(alumno, pk=pk)
    if request.method == 'POST':
        alumno_obj.delete()
        return redirect('alumno_list')
    return render(request, 'alumno_confirm_delete.html', {'alumno': alumno_obj})
