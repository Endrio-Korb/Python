"""
Trabalhando com arquivos em csv

reader e DictReader

CSV -> Comma Separated Values -> Valores separados por virgula
"""

import csv
import os


if __name__ == "__main__":

    with open(os.path.join(os.getcwd(), "notas.csv"), "r") as arquivo:
        
        # Por padrão o método reader considera que o separador padrão é a virgula
        # Nesse caso, precisamos indicar que o separador padrão é o ponto-e-virgula
        arquivo_csv = csv.reader(arquivo, delimiter =';')

        for linha in arquivo_csv:
            print(linha)

    with open(os.path.join(os.getcwd(), "notas.csv"), "r") as arquivo:
        
        # Para usar o DictReader ele deve ser escrito extamente desta maneira
        # utilizando as letras maisculas como o exemplo -> DictReader
        arquivo_csv = csv.DictReader(arquivo, delimiter=";")

        for linha in arquivo_csv:
            print(linha)