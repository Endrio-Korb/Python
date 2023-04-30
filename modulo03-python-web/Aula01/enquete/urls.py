from django.urls import path

# O ponto significa que iremos importa o modulo view que se encontra no mesmo diretório 
# que o modulo views
from . import views



urlpatterns = [
    path("numero-da-sorte", views.numero_da_sorte, name="numero_da_sorte"),
    path("", views.index, name="index"),
]