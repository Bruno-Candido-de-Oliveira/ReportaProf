from django.db import models

class Dependencia(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return f'ID: {self.id} - {self.nome}'
    
class Turma(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20)
    turno = models.CharField(max_length=20)
    sala = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.id} - Turma: {self.nome} - Turno: {self.turno} - Sala: {self.sala}'

class Estudante(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    turma = models.ForeignKey(Turma, related_name='estudantes', on_delete=models.CASCADE)
    nascimento = models.DateField()
    ativo = models.BooleanField("Ativo")

    def __str__(self):
        return f'{self.nome} - Nascimento: {self.nascimento} - Ativo: {self.ativo} - TURMA: {self.turma}'

class Disciplina(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return f'ID: {self.id} - {self.nome}'
    

class Professor(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.id} - {self.nome}'
    
class TurmaDisciplina(models.Model):
    id = models.AutoField(primary_key=True)
    turma = models.ForeignKey(Turma, related_name='turma_disciplinas', on_delete=models.PROTECT)
    disciplina = models.ForeignKey(Disciplina, related_name='turma_disciplinas', on_delete=models.PROTECT)
    professor = models.ForeignKey(Professor, related_name='turma_disciplinas', on_delete=models.PROTECT)
    
    def __str__(self):
        return f'ID: {self.id} - TURMA: {self.turma} - DISCIPLINA: {self.disciplina} - PROFESSOR: {self.professor}'
    
class Situacao(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Ocorrencia(models.Model):
    id = models.AutoField(primary_key=True)
    data_hora = models.DateTimeField(auto_now=True)
    professor = models.ForeignKey(Professor, related_name='ocorrencia', on_delete=models.PROTECT)
    turma = models.ForeignKey(Turma, related_name='ocorrencia', on_delete=models.PROTECT)
    dependencia = models.ForeignKey(Dependencia, related_name='ocorrencia', on_delete=models.PROTECT, null=True, blank=True)
    estudantes = models.ManyToManyField(Estudante, related_name='ocorrencia')
    situacao = models.ManyToManyField(Situacao, related_name='ocorrencia')
    observacao = models.TextField(max_length=300, blank=True)
    
    def __str__(self):
        return f'{self.id} - {self.data_hora} - {self.professor} - {self.turma} - {self.dependencia} - {self.estudantes} - {self.situacao} - {self.observacao}'


    