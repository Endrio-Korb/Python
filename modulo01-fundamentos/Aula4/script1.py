"""
Funções lambda

Funções lambda são funções que não possuem nome. Utilizamos a 
palavra reservada lambda
"""
from random import randint

def quadrado(numero):
    return numero ** 2

if __name__ == "__main__":

    #Criar uma lista de números randômicos utilizando list-comprehension
    lista_randomico = [randint(1,10) for _ in range(20)]

    """
    O código acima é a mesma coisa que:
    lista_randomico = []
    for _ in range(100):
        lista_randomico.append(randint(1,100))
    """

    nova_lista = []

    for numero in lista_randomico:
        nova_lista.append(quadrado(numero))

    print("Lista de quadrado utilizando a função quadrad()")
    print(nova_lista)

    # Criar uma função lambda(anonima) que retorna o quadrado do argumento x
    # A função map() recebe dois argumentos: A função que será aplicada a cada
    # item da sequencia, e a sequencia em si
    # No caso abaixo, a função map*() vai multiplicar cada item da sequencia por ele mesmo
    nova_lista = list(map(lambda x: x * x, lista_randomico))
    print("Lista de quadrados utilizando map() e lambda")
    print(nova_lista)

    quatro = lambda x: x ** 2
    print(quatro(10))

    cinco = lambda x,y : x / y
    print(cinco(10,2))

    print("="*50)  

    # Criar uma lista apenas com os números pares da nova_lista
    # A função filter aplica uma função para cada item da sequência.
    # Cas essa função retorne o valor booleano True, o valor dessa lista é retornado.
    nova_lista_pares = filter(lambda x: x % 2 == 0, nova_lista)
    print("Lista de pares")
    print(list(nova_lista_pares))
    
    print("="*50)

    nova_lista_impares = filter(lambda x: x % 2 != 0, nova_lista)
    print("Lista impares")
    print(list(nova_lista_impares))

