from django.urls import path

# O ponto (.) significa que iremos importar o módulo views que se encontra no mesmo
# diretório que o módulo urls
from . import views

# name space
app_name = "mensagens"

urlpatterns = [
    path("inserir_comentario", views.inserir_comentario, name="inserir_comentario")
]
