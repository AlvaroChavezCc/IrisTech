from django.urls import path

from profesor import views

urlpatterns = [
    path('', views.profesor_inicio, name="profesor_inicio"),
    #Esto hace que se tome un valor buscado como parámetro (<int:id>).
    path('login/', views.login_view, name='login_p'),
    path('logout/', views.logout_view, name='logout_p'),
    path('resetear/', views.resetear, name="reset"),
    path('cursos/<int:curso_id>/tareas/', views.tareas_curso, name='tareas_curso'),
    path('tareas/crear/<int:curso_id>/', views.crear_tarea, name='crear_tarea'),
    path('cursos/', views.cursos, name='cursos'),
    path('tareas/<int:curso_id>/', views.tareas_curso, name='tareas_curso'),
    path('tareas/editar/<int:tarea_id>/', views.editar_tarea, name='editar_tarea'),
    path('tareas/eliminar/<int:tarea_id>/', views.eliminar_tarea, name='eliminar_tarea'),
    path('tarea/<int:tarea_id>/evaluaciones/', views.visualizar_evaluaciones, name='visualizar_evaluaciones'),
    path('evaluar-tarea/<int:tarea_id>/', views.evaluate_tarea, name='evaluar_tarea'),
    path('ver-respuesta/<int:evaluacion_id>/', views.ver_respuesta, name='ver_respuesta'),
    path('evaluacion/<int:evaluacion_id>/evaluar_manualmente/', views.evaluar_manualmente, name='evaluar_manualmente'),
    path('evaluar-todas/<int:tarea_id>/', views.evaluate_tarea, name='evaluar_todas'),
    path('reclamos/', views.lista_reclamos, name='lista_reclamos'),
    path('reclamos/atender/<int:reclamo_id>/', views.atender_reclamo, name='atender_reclamo'),
    path('reclamos/justificar/<int:reclamo_id>/', views.justificar_nota, name='justificar_nota'),
    path('reclamos/modificar/<int:reclamo_id>/', views.modificar_nota, name='modificar_nota'),
]