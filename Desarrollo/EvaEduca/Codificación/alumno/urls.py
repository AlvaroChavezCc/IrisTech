from django.urls import path
from alumno import views

urlpatterns = [
    path('', views.inicio, name="alumno"),
    
    path('login/', views.login_alumno, name='login_alumno'),
    path('logout/', views.logout_alumno, name='logout_alumno'),
    path('descargar-examen/', views.descargar_examen, name='descargar_examen'),
    path('cargar-respuesta/<int:tareas_id>/', views.cargar_respuesta, name='cargar_respuesta'),
]
