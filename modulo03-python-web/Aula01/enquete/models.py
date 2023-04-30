from django.db import models

# Create your models here.

class Pergunta(models.Model):

    texto = models.CharField(max_length=200)
    data_de_publicacao = models.DateField("Data de Publicação")

    # A classe Meta representa as configurações da model
    class Meta:
        db_table = "tb_perguntas"