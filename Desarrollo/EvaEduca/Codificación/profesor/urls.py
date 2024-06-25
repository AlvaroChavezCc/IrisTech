from django.urls import path

from profesor import views

urlpatterns = [
    path('', views.inicio, name="profesor"),

    #Esto hace que se tome un valor buscado como parámetro (<int:id>).
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('resetear/', views.resetear, name="reset"),
    path('cursos/<int:curso_id>/tareas/', views.tareas_curso, name='tareas_curso'),
    path('tareas/crear/<int:curso_id>/', views.crear_tarea, name='crear_tarea'),
    path('cursos/', views.cursos, name='cursos'),
    path('tareas/<int:curso_id>/', views.tareas_curso, name='tareas_curso'),
    path('tareas/editar/<int:tarea_id>/', views.editar_tarea, name='editar_tarea'),
    path('tareas/eliminar/<int:tarea_id>/', views.eliminar_tarea, name='eliminar_tarea'),
    path('evaluar-tarea/<int:tarea_id>/', views.evaluate_tarea, name='evaluar_tarea'),
]