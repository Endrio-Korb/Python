from django.urls import path

from . import views

app_name = "cursos"

urlpatterns = [
    path("", views.cursos, name="cursos"),
    path("matriculas/", views.matriculas, name="matriculas"),
]
