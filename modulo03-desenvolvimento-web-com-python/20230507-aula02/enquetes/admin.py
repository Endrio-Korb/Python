from django.contrib import admin
# Register your models here.

from enquetes.models import Pergunta, Opcao

admin.site.register(Pergunta)
admin.site.register(Opcao)