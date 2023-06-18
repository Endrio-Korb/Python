from django.db import models

class Cursos(models.Model):

    nome = models.CharField(max_length=100, null=False, blank=False)
    carga_horaria = models.FloatField(null=False, blank=False)
    preco = models.FloatField(null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)

    class Meta:

        db_table = "tb_cursos"

    def __str__(self):
        return self.nome


