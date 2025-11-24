from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('turmas/', views.get_turmas, name='get_turmas'),
    path('turmas/<int:pk>/estudantes/', views.get_alunos_disciplina),
    path('dependencias/', views.get_dependencias, name='get_dependencias'),
    path('situacoes/', views.get_situacoes, name='get_situacoes'),
    path('ocorrencias/', views.get_ocorrencias, name='get_ocorrencias'),
    path('ocorrencia/<int:pk>', views.get_ocorrencia_id, name='get_ocorrencia_id'),
    path('ocorrencias/novo', views.new_ocorrencia, name='set_ocorrencias'),
]