"""
Crie um script que abra o arquivo vendas.txt e leio o seu conteúdo. O conteúdo do arquivo é formado por uma lista de informações sobre vendedores: O seu código, o seu nome e a quantidade de vendas realizadas em um período. O script deve mostrar no terminal as seguintes informações:
Valor total de vendas (soma das vendas de todos os vendedores)
Média total de vendas
Lista dos maiores vendedores, do maior pro menor
Além disso, deve ser calculado o valor total da remuneração do vendedor de acordo com as seguintes regras:

Vendedores que venderam menos de 5000, não recebem bônus
Vendedores que venderam entre 5000 e 9999.99, recebem um bônus de 10%
Vendedores que venderam entre 10000 e 14999.99, recebem um bônus de 20%
Vendedores que venderam 15000 ou mais, recebem um bônus de 30% Além disso, os 3 primeiros colocados recebem como um adicional no salário os seguintes valores, na ordem:
500 para o primeiro colocado em vendas
250 para o segundo colocado em vendas
125 para o terceiro colocado em vendas
Essas informações devem ser mostradas no terminal
"""

import os

# Criar uma função que junta os numeros
def junta_numeros( lista_vendas):
        total_vendas = 0
        
        #for linha in lista_vendas:
          #  numeros_juntos = linha.translate(str.maketrans('','', string.punctuation))

        for linha in  lista_vendas:
            for letra in linha:
                if letra == "1":
                    letra = 1
                    numeros_juntos.append(letra)
                elif letra == "2":
                    letra = 2
                    numeros_juntos.append(letra)
                elif letra == "3":
                    letra = 3
                    numeros_juntos.append(letra)
                elif letra == "4":
                    letra = 4
                    numeros_juntos.append(letra)
                elif letra == "5":
                    letra = 5
                    numeros_juntos.append(letra)
                elif letra == "6":
                    letra = 6
                    numeros_juntos.append(letra)
                elif letra == "7":
                    letra = 7
                    numeros_juntos.append(letra)
                elif letra == "8":
                    letra = 8
                    numeros_juntos.append(letra)
                elif letra == "9":
                    letra = 9
                    numeros_juntos.append(letra)
                elif letra == ".":
                  pass
                else:
                    pass

        for i in numeros_juntos:
            total_vendas =  total_vendas + i



if __name__ == "__main__":

    lista_dados = []
    numeros_juntos = []



    with open(os.path.join(os.getcwd(), "vendas.txt"), "r", encoding= "utf-8") as arquivo:

        # for i, linha in enumerate(arquivo):
        #     print(f'{str(i)}: {str(linha)}')

        # print("=" * 100)

        # for linha in(arquivo):
        #     lista_dados.append(str(linha))
        # print(lista_dados)
        texto = arquivo.readlines()
        
        lista_vendas = []
        lista_vendas_nova = []

        for linha in texto:
            if "Vendas" in linha:
                lista_vendas.append(linha[8:13])
        
        print(junta_numeros(lista_vendas))
        #lista_vendas_nova.append(float(linha) for linha in lista_vendas)


      
        
