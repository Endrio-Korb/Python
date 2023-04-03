"""
Crie um script que abra o arquivo nomes.txt e leia o seu conteúdo. Depois de lido,
você deve imprimir no terminal os 10 nomes que mais se repetem e a quantidade de vezes 
que eles se repetem na ordem do maior pro menor. Exemplo:
python ex01.py
Lista de nomes que mais se repetem:

Mariane: 10 vezes
Manuela: 9 vezes
Heitor: 6 vezes
Além disso, essas informações devem ser salvas em um arquivo csv (nomes.csv), que vai conter 2 colunas:

nome
quantidade
Dica: Salve os dados em um dicionário e utilize a função built-in sorted() para mostrar na ordem correta.
"""

import os
from operator import itemgetter
import codecs


if __name__ == "__main__":

    with open(os.path.join(os.getcwd(),"nomes.txt"), "r") as arquivo:
        arquivo = codecs.open('nomes.txt', 'rb', encoding='utf-8')

        dict_nomes = {}
        lista_nome = []
        lista_quant = []
        novo_dict = {}
        for nome in arquivo:
            if dict_nomes.get(nome):
                dict_nomes[nome] += 1
            else: 
                dict_nomes[nome] = 1
        
        dict_nome_ordenado = {}
        for i in sorted(dict_nomes, key = dict_nomes.get, reverse= True):
            dict_nome_ordenado[i] = dict_nomes[i]
        
        for i in dict_nome_ordenado.keys():
            lista_nome.append(i[:-2])
        for i in dict_nome_ordenado.values():
            lista_quant.append(i)
        for i in range(10):
            novo_dict.update({lista_nome[i] : lista_quant[i]})


        print(novo_dict)