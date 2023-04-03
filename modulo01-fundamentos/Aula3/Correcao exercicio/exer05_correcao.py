from random import randint

def func(lista):
    dict_numeros = {}

    for numero in lista:
        if dict_numeros.get(numero):
            dict_numeros[numero] += 1
        else:
            dict_numeros[numero] = 1
    
    """
    Salvando o item que mais aparece em uma variavel
    """
    maior = 0
    vezes = 0

    for chave,valor in dict_numeros.items():
        if valor >= vezes:
            vezes = valor
            maior = chave
    
    return maior, vezes

if __name__ == "__main__":
    
    lista = [randint(1,10) for _ in range(200)]
    mais_aparece, vezes = func(lista)
    print(f"O valor que mais aparece é o {mais_aparece} e o número de vezes é de {vezes}")