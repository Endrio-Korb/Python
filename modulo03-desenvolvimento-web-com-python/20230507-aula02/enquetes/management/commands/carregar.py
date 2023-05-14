import json
import os

from django.core.management.base import BaseCommand

from enquetes.models import Pergunta, Opcao


class Command(BaseCommand):

    help = "Carregar arquivos e salva no banco de dados"

    def add_arguments(self, parser):
        parser.add_argument("arquivo", nargs=1, type=str)

    def handle(self, *args, **options):
        
        arquivo = options.get("arquivo")
        caminho_arquivo = os.path.join(os.getcwd(), arquivo)

        with open(caminho_arquivo, "r", encoding="utf-8") as _f:

            conteudo_arquivo = json.load(_f)

            for pergunta, opcoes in conteudo_arquivo.items():
                self.stdout.write(pergunta, opcoes)
