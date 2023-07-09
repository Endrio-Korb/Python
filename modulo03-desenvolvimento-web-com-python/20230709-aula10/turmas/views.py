from django.shortcuts import render


def turmas(request):
    lista_de_turmas_matriculada = request.user.aluno.all()

    return render(request,"turmas.html", {"lista_de_turmas_matriculada": lista_de_turmas_matriculada})