from django.shortcuts import render
from turmas.models import Turma
from cursos.models import Curso

def turmas(request):

    lista_de_turmas = Turma.objects.all()


    return render(request,"turmas.html", {"lista_de_turmas": lista_de_turmas})