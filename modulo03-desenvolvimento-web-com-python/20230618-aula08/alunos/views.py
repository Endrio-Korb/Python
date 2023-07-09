from django.shortcuts import render

from turmas.models import Turma


def perfil(request):

    lista_de_matricula = request.user.aluno.all()

    return render(request, "perfil.html", {"lista_de_matricula": lista_de_matricula})
