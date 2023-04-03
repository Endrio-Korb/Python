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

    lista_nota = []
    qt_alunos = []

    with open(os.path.join(os.getcwd(), "notas.csv"), "r") as arquivo:
        arquivo_csv = csv.reader(arquivo, delimiter=";")
        
        for i , linha in enumerate(arquivo_csv):
            if i == 0:
              pass
              # Imprimi cabeçalho
              #  print("Cabeçalho" + str(linha))
            else:
                lista_nota.append((linha[1:6]))
                qt_alunos.append(linha[0])
                # Imprimir a aluno: notas
                #print("Aluno:" + str(linha))

        print(f"A quantidade de alunos é de {len(qt_alunos)} alunos")
        
        lista_nota.sort(reverse = True)

        nova_lista_nota = []
        media_total = 0
        for linha in  lista_nota:
            for letra in linha:
                if letra == "1":
                    letra = 1
                    nova_lista_nota.append(letra)
                elif letra == "2":
                    letra = 2
                    nova_lista_nota.append(letra)
                elif letra == "3":
                    letra = 3
                    nova_lista_nota.append(letra)
                elif letra == "4":
                    letra = 4
                    nova_lista_nota.append(letra)
                elif letra == "5":
                    letra = 5
                    nova_lista_nota.append(letra)
                elif letra == "6":
                    letra = 6
                    nova_lista_nota.append(letra)
                elif letra == "7":
                    letra = 7
                    nova_lista_nota.append(letra)
                elif letra == "8":
                    letra = 8
                    nova_lista_nota.append(letra)
                elif letra == "9":
                    letra = 9
                    nova_lista_nota.append(letra)
                elif letra == "10":
                    letra = 10
                    nova_lista_nota.append(letra)
                else:
                    pass

        for i in nova_lista_nota:
            media_total += i
        
        media_final = media_total / len(nova_lista_nota)
        print(f'A média geral dos alunos é de: {media_final:.2f}')
        print(nova_lista_nota)
