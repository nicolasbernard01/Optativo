from django.urls import path
from . import views

urlpatterns = [

    path('inicio/', views.inicio,name='inicio'),
    path('cursos/', views.cursos,name='cursos'),
    path('eventos/', views.eventos,name='eventos'),
    #path('contacto/', views.contacto,name='contacto'),

]

