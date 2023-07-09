from django.shortcuts import render

def perfil(request):

    lista_de_turmas_matriculada = request.user.aluno.all()
    
    return render(
        request,
        "perfil.html",
        {"lista_de_turmas_matriculada": lista_de_turmas_matriculada}
    )
