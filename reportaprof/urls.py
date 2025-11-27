from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from .views import (TurmaList, DependenciasList, EstudantesTurmasList, OcorrenciasList, OcorrenciasProfessor,
                    TurmaProfessorList, SituacoesList, OcorrenciaIdView, NovaOcorrencia, EditOcorrencia, OcorrenciasEstudante)


from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Pastebin API",
        default_version='v1',
        description="API description",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('turmas/', TurmaList.as_view(), name='turma-list'),
    path('turmas/<int:pk>/estudantes/', EstudantesTurmasList.as_view(), name='estudantes-disciplina-list'),
    path('turmas/<int:pk>/professor', TurmaProfessorList.as_view(), name='turma-professor-list'),
    path('dependencias/', DependenciasList.as_view(), name='dependencia-list'),
    path('situacoes/', SituacoesList.as_view(), name='situacoes.list'),
    path('ocorrencias/', OcorrenciasList.as_view(), name='ocorrencias-list'),
    path('ocorrencia/<int:pk>', OcorrenciaIdView.as_view(), name='ocorrencia-id-view'),
    path('ocorrencias/novo', NovaOcorrencia.as_view(), name='nova-ocorrencia'),
    path('ocorrencia/<int:pk>/edit', EditOcorrencia.as_view(), name='edit-ocorrencia'),
    path('ocorrencias/<int:pk>/professor', OcorrenciasProfessor.as_view(), name='ocorrencias-professor'),
    path('ocorrencias/<int:pk>/estudante', OcorrenciasEstudante.as_view(), name='ocorrencias-estudante'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]







