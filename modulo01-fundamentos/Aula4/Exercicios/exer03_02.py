"""
Crie um script que abra o arquivo notas.csv e leia o seu conteúdo. O arquivo possui uma 
lista de nomes de alunos e as suas respectivas novas em trabalhos. Depois de ler esse arquivo, 
o script deve mostrar:
A quantidade total de alunos
A média geral
Os 10 alunos com as maiores médias Detalhe: As médias são calculadas excluindo a melhor e a
 pior nota de cada aluno. Ou seja, a média é calculada utilizando as 3 notas intermediárias. 
Dica: Ordene as notas ou utilize as funções built-in max() e min() para saber quais são
as melhores e as piores notas
"""

import os
import csv 


if __name__ == "__main__":

    dict_alunos = {}

    with open(os.path.join(os.getcwd(), "notas.csv"),"r") as arquivo:
        arquivo_csv = csv.DictReader(arquivo, delimiter = ";")

      