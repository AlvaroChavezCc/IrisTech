from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import curso
from profesor.models import profesor
from .forms import CursoForm, ProfesorForm, LoginForm

# Vista de Redirección
def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return redirect('curso_list')

# Vistas de Login
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('curso_list')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

# Vistas de Profesor
def profesor_list(request):
    profesores = profesor.objects.all()
    return render(request, 'profesor_list.html', {'profesores': profesores})

def profesor_create(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profesor_list')
    else:
        form = ProfesorForm()
    return render(request, 'profesor_form.html', {'form': form})

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

def profesor_delete(request, pk):
    profesor_obj = get_object_or_404(profesor, pk=pk)
    if request.method == 'POST':
        profesor_obj.delete()
        return redirect('profesor_list')
    return render(request, 'profesor_confirm_delete.html', {'profesor': profesor_obj})

# Vistas de Curso
def curso_list(request):
    cursos = curso.objects.all()
    return render(request, 'curso_list.html', {'cursos': cursos})

def curso_create(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('curso_list')
    else:
        form = CursoForm()
    return render(request, 'curso_form.html', {'form': form})

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

def curso_delete(request, pk):
    curso_obj = get_object_or_404(curso, pk=pk)
    if request.method == 'POST':
        curso_obj.delete()
        return redirect('curso_list')
    return render(request, 'curso_confirm_delete.html', {'curso': curso_obj})
