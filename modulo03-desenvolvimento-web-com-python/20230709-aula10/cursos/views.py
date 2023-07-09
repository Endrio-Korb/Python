from django.shortcuts import render, get_object_or_404
from cursos.models import Curso


def cursos(request):

    lista_de_cursos = Curso.objects.all()

    return render(request,"cursos.html", {"lista_de_cursos": lista_de_cursos})



def detalhes_curso(request, curso_id):
    curso = get_object_or_404(Curso, pk=curso_id )

    lista_de_turmas = curso.turma_set.filter(aceitando_matriculas=True)

    return render(request, "detalhes.html",{"lista_de_turmas":lista_de_turmas})


