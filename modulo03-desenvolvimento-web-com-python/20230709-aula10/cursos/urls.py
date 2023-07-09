from django.urls import path

from . import views

app_name = "cursos"

urlpatterns = [
    path("cursos/", views.cursos, name="cursos"),
]
