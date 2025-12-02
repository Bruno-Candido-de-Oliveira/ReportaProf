from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Estudante, Turma, TurmaDisciplina, Situacao, Ocorrencia, Dependencia, Professor
from .serializers import (EstudanteSerializer, TurmaSerializer, TurmaDisciplinaSerializer, SituacaoSerializer,
                          GetOcorrenciaSerializer, PostOcorrenciaSerializer, DependenciaSerializer)

from django.urls import path
from rest_framework_swagger.views import get_swagger_view
        
class TurmaList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer

class DependenciasList(generics.ListAPIView):
    queryset = Dependencia.objects.all()
    serializer_class = DependenciaSerializer
    
class EstudantesTurmasList(generics.ListAPIView):
    serializer_class = EstudanteSerializer
    
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        turma_disciplina = get_object_or_404(TurmaDisciplina, pk=pk)
        return Estudante.objects.filter(turma = turma_disciplina.turma_id)


class OcorrenciasProfessor(generics.ListAPIView):
    serializer_class = GetOcorrenciaSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        professor_logado = self.request.user.professor
        return Ocorrencia.objects.filter(professor = professor_logado)
    
class OcorrenciasProfessorID(generics.ListAPIView):
    serializer_class = GetOcorrenciaSerializer
    
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        professor = get_object_or_404(Professor, pk=pk)
        return Ocorrencia.objects.filter(professor = professor.id)

class OcorrenciasEstudante(generics.ListAPIView):
    serializer_class = GetOcorrenciaSerializer
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        estudante = get_object_or_404(Estudante, pk=pk)
        return Ocorrencia.objects.filter(estudantes = estudante.id)
        
class TurmaProfessorList(generics.ListAPIView):
    serializer_class = TurmaDisciplinaSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        professor_logado = self.request.user.professor
        return TurmaDisciplina.objects.filter(professor = professor_logado)

class TurmaProfessorListID(generics.ListAPIView):
    serializer_class = TurmaDisciplinaSerializer
    
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        professor = get_object_or_404(Professor, pk=pk)
        return TurmaDisciplina.objects.filter(professor = professor.id)

class SituacoesList(generics.ListAPIView):
    queryset = Situacao.objects.all()
    serializer_class = SituacaoSerializer

class OcorrenciasList(generics.ListAPIView):
    queryset = Ocorrencia.objects.all()
    serializer_class = GetOcorrenciaSerializer

class OcorrenciaIdView(generics.RetrieveAPIView):
    queryset = Ocorrencia.objects.all()
    serializer_class = GetOcorrenciaSerializer

class NovaOcorrencia(generics.CreateAPIView):
    serializer_class = PostOcorrenciaSerializer
    queryset = Ocorrencia.objects.all()

class EditOcorrencia(generics.UpdateAPIView):
    queryset = Ocorrencia.objects.all()
    serializer_class = PostOcorrenciaSerializer