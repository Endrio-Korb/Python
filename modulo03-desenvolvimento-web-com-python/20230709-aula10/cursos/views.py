from django.shortcuts import render
from cursos.models import Curso

def cursos(request):

    lista_de_turmas_matriculada = request.user.aluno.all()
    lista_de_cursos = Curso.objects.all()

    return render(request,"cursos.html", {"lista_de_cursos": lista_de_cursos,"lista_de_turmas_matriculada":lista_de_turmas_matriculada})