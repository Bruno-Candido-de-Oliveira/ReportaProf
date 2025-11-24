from django.contrib import admin
from .models import Estudante, Professor, Turma, Disciplina, TurmaDisciplina, Ocorrencia, Situacao, Dependencia

admin.site.register(Estudante)
admin.site.register(Professor)
admin.site.register(Turma)
admin.site.register(Dependencia)
admin.site.register(Disciplina)
admin.site.register(TurmaDisciplina)
admin.site.register(Ocorrencia)
admin.site.register(Situacao)


