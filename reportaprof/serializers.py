from rest_framework import serializers

from .models import Estudante, Professor, Turma, Disciplina, TurmaDisciplina, Ocorrencia, Situacao, Dependencia


class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'nome']

class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = '__all__'

class DependenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dependencia
        fields = '__all__'
        
class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = '__all__'

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'

class TurmaDisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TurmaDisciplina
        fields = '__all__'

class SituacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Situacao
        fields = '__all__'
        
class PostOcorrenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocorrencia
        fields = '__all__'

class GetOcorrenciaSerializer(serializers.ModelSerializer):
    professor = ProfessorSerializer()
    turma = TurmaSerializer()
    estudantes = EstudanteSerializer(many=True)
    situacao = SituacaoSerializer(many=True)
    dependencia = DependenciaSerializer()
    class Meta:
        model = Ocorrencia
        fields = '__all__'