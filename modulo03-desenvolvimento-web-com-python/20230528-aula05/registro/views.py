from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from registro.forms import PreRegistroForm
from registro.models import PreRegistro

from registro.validators import dados_preenchidos, username_ou_email_ja_cadastrador, senha_valida

def registrar(request):

    if request.method == "GET":
        return render(request, "registro.html")

    elif request.method == "POST":
        
        try:
            username = request.POST['username']
            email = request.POST['email']
            senha = request.POST['password1']
            confirmacao_senha = request.POST['password2']

            error_message = None
            
            if not dados_preenchidos(username,email,senha,confirmacao_senha):
                error_message = "Todos os campos são origatórios."

            elif username_ou_email_ja_cadastrador(username, email):
                error_message = "Existe algum problema no seu cadastro."

            elif not senha_valida(senha, confirmacao_senha):
                error_message = "As senhas não conferem."

            if error_message:
                return render(request, 'registro.html', {'error_message': error_message})

            User.objects.create_user(
                username=username, email=email, password=senha
            )

            return redirect("login")

        except Exception:
            pass


def pre_registro(request):

    if request.method == "GET":
        form = PreRegistroForm()
        return render(request, "pre_registro.html", {"form": form})

    elif request.method == "POST":
        
        form = PreRegistroForm(request.POST)

        if form.is_valid():

            email = form.cleaned_data.get("email")

            email_ja_cadastrado = User.objects.filter(email=email)
            email_no_pre_cadastro = PreRegistro.objects.filter(email=email)

            if email_ja_cadastrado or email_no_pre_cadastro:

                form.errors.update({
                    "Erro de Pré-cadastro":"O e-mail informado é inválido. Verifique se o e-mail já não está cadastrado ou faz parta do pré-cadastro."
                })

                return render(request, "pre_registro.html",{"form":form})
            
            pre_registro = PreRegistro(email=email)
            pre_registro.save()

            menssagem_email = f"""
            Você recebeu esse e-mail pois você ou alguém cadastro no sistema de agendamento.
            Caso queira confirma o cadastro, clique no link a seguir.
            Caso não tenha sido você, apenas ignore esse e-mail.


            http://127.0.0.1:8000/registro/confirmacao?id={pre_registro.uuid}

            """

            # send_mail(
            #     assunto,
            #     menssagem,
            #     quem vai mandar,
            #     quem vai receber,
            # )

            send_mail(
                "Bem-vindo ao sistema de agendamento",
                menssagem_email,
                "admin@localhost",
                [pre_registro.email]
            )

            return render(request, "envio_pre_cadastro.html")