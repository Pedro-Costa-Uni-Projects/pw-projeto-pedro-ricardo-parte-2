from django.shortcuts import render
from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('home', views.home_page_view, name='home'),
    path('benificios', views.benificios_page_view, name='benificios'),
    path('about', views.about_page_view, name='about'),
    path('comentarios', views.comentarios_page_view, name='comentarios'),
    path('estilos', views.estilos_page_view, name='estilos'),
    path('galeria', views.galeria_page_view, name='galeria'),
    path('provas', views.provas_page_view, name='provas'),
    path('quizz', views.quizz_page_view, name='quizz'),
    path('contacto', views.contacto_page_view, name='contacto'),
]
