from django.contrib.auth.models import User
from django.db import models

from cursos.models import Cursos

class Turma(models.Model):

        curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
        instrutor = models.ForeignKey(User, on_delete=models.CASCADE)
        data_inicio = models.DateTimeField(null=False, blank=False)
        data_fim = models.DateTimeField(null=False, blank=False)
        qtd_minimo_alunos = models.IntegerField(default=0)
        qtd_maxima_alunos = models.IntegerField(default=100)

        class Meta:
            db_table = "tb_turmas"

        def __str__(self):
              return f"Turma {self.data_inicio.year}{self.id} {self.curso}"