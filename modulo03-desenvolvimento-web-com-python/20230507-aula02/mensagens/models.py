from django.db import models

from enquetes.models import Pergunta

class Mensagens(models.Model):

    email = models.CharField(max_length=100, null=True)    
    texto = models.CharField(max_length=200, null=False)
    data_hora = models.DateTimeField(auto_now_add=True)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)

    class Meta:
        db_table = "tb_mensagens"


    