
from django.urls import path

from . import views

app_name = "registro"

urlpatterns = [
    path("pre_registro/", views.pre_registro, name="pre_registro"),  
    path("",views.confirmacao, name="confirmacao")  
]