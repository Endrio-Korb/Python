from django.urls import path

from . import views

app_name = "cursos"

urlpatterns = [
    path("", views.cursos, name="cursos"),
    path("<int:curso_id>/detalhes/", views.detalhes_curso, name="detalhes"),
]
