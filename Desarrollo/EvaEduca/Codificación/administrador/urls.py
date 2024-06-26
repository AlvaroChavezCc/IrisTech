from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # URL base que redirige al login si no autenticado
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # URLs de Profesor
    path('profesores/', views.profesor_list, name='profesor_list'),
    path('profesores/nuevo/', views.profesor_create, name='profesor_create'),
    path('profesores/<int:pk>/editar/', views.profesor_update, name='profesor_update'),
    path('profesores/<int:pk>/eliminar/', views.profesor_delete, name='profesor_delete'),

    # URLs de Curso
    path('cursos/', views.curso_list, name='curso_list'),
    path('cursos/nuevo/', views.curso_create, name='curso_create'),
    path('cursos/<int:pk>/editar/', views.curso_update, name='curso_update'),
    path('cursos/<int:pk>/eliminar/', views.curso_delete, name='curso_delete'),
]
