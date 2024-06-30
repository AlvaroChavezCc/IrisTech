from django.urls import path
from alumno import views

urlpatterns = [
      
    path('login/', views.login_alumno, name='login_alumno'),
    path('logout/', views.logout_alumno, name='logout_alumno'),
    path('bienvenida/', views.bienvenida, name='bienvenida_alumno'),
    path('subir_respuesta/', views.subir_respuesta, name='subir_respuesta'),
    path('tareas/', views.lista_tareas, name='lista_tareas'),
]
