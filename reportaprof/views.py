from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Estudante, Turma, TurmaDisciplina, Situacao, Ocorrencia, Dependencia, Professor
from .serializers import (EstudanteSerializer, TurmaSerializer, TurmaDisciplinaSerializer, SituacaoSerializer,
                          GetOcorrenciaSerializer, PostOcorrenciaSerializer, DependenciaSerializer)

from django.urls import path
from rest_framework_swagger.views import get_swagger_view

import json

'''class TurmaList(APIView):
    def get(self, request):
        turmas = Turma.objects.all()
        serializer = TurmaSerializer(turmas, many=True)
        return Response(serializer.data)'''
        
class TurmaList(generics.ListAPIView):
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
    
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        professor = get_object_or_404(Professor, pk=pk)
        return Ocorrencia.objects.filter(professor = professor.id)
    
    
class TurmaProfessorList(generics.ListAPIView):
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

class OcorrenciaIdView(generics.ListAPIView):
    serializer_class = Ocorrencia
    
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        ocorrencia = Ocorrencia.objects.filter(pk = pk)

@api_view(['GET'])
def get_ocorrencia_id(request, pk):
    try:
        ocorrencia = Ocorrencia.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = GetOcorrenciaSerializer(ocorrencia)
    return Response(serializer.data)

@api_view(['POST'])
def new_ocorrencia(request):
    ocorrencia = request.data
    serializer = PostOcorrenciaSerializer(data=ocorrencia)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def edit_ocorrencia(request, pk):
    try:
        ocorrencia = Ocorrencia.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = PostOcorrenciaSerializer(ocorrencia, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)





    