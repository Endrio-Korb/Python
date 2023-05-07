from random import randint

from django.shortcuts import render

from django.http import HttpResponse

from enquetes.models import Pergunta

# Create your views here.

# enquetes/numero-da-sorte -- teste
def numero_da_sorte(request):
    numero_da_sorte = randint(1, 60)

    return HttpResponse(numero_da_sorte)


def index(request):
    ultimas_cincos_perguntas = Pergunta.objects.order_by("-data_de_publicacao")[:5]
    saida = ", ".join([p.texto for p in ultimas_cincos_perguntas])
    return HttpResponse(saida)

def detalhes(request, pergunta_id):
    return HttpResponse(f"Você está acessando os detalhes da pergunta {pergunta_id}")

def resultados(request, pergunta_id):
    return HttpResponse(f"Você está olhando os resultado da pergunta {pergunta_id}")

def votar(request, pergunta_id):
    return HttpResponse(f"Você está votando na pergunta {pergunta_id}")
