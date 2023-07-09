from django.urls import path

from . import views

app_name = "turmas"

urlpatterns = [
    path("", views.turmas, name="turmas"),
]
