from django import views
from django.urls import path
from . import views


urlpatterns= [
    path('', views.inicio, name='inicio'),
    path('acerca/', views.acerca, name='acerca'),
    path('profesionales/', views.profesionales, name='profesionales'),
    path('detalleMedico/', views.detalleMedico, name='detalleMedico'),
    path('receta/', views.receta, name='receta'),
    path('ubicacion/', views.ubicacion, name='ubicacion'),
    
    path('galeria/', views.galeria, name='galeria'),
    path('testimonio/', views.testimonio, name='testimonio'),
    
    
    
]