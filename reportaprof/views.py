from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Estudante, Turma, TurmaDisciplina, Situacao, Ocorrencia, Dependencia, Professor
from .serializers import (EstudanteSerializer, TurmaSerializer, TurmaDisciplinaSerializer, SituacaoSerializer,
                          GetOcorrenciaSerializer, PostOcorrenciaSerializer, DependenciaSerializer)

import json

@api_view(['GET'])
def get_turmas(request):
    turmas = Turma.objects.all()
    serializer = TurmaSerializer(turmas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_dependencias(request):
    dependencias = Dependencia.objects.all()
    serializer = DependenciaSerializer(dependencias, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def get_alunos_disciplina(request, pk):
    try:
        turma_disciplina = TurmaDisciplina.objects.get(pk=pk)
    except:
         return Response(status=status.HTTP_404_NOT_FOUND)

    estudantes = Estudante.objects.filter(turma=turma_disciplina.turma_id)

    serializer = EstudanteSerializer(estudantes, many=True)
    if serializer.data:
        return Response(serializer.data)
    return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_ocorrencia_professor(request, pk):
    try:
        professor = Professor.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    ocorrencias = Ocorrencia.objects.filter(professor=professor.id)

    serializer = GetOcorrenciaSerializer(ocorrencias, many=True)
    if serializer.data:
        return Response(serializer.data)
    return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_turma_professor(request, pk):
    try:
        professor = Professor.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    turmas = TurmaDisciplina.objects.filter(professor=professor.id)
    serializer = TurmaDisciplinaSerializer(turmas, many=True)
    if serializer.data:
        return Response(serializer.data)
    return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_situacoes(request):
    situacoes = Situacao.objects.all()
    serializer = SituacaoSerializer(situacoes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_ocorrencias(request):
    ocorrencias = Ocorrencia.objects.all()
    serializer = GetOcorrenciaSerializer(ocorrencias, many=True)
    return Response(serializer.data)

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

    