def highest_rank(lista):
    dict_numeros = {}
    
    for numero in lista:
        if dict_numeros.get(numero):
            dict_numeros[numero] += 1
        else:
            dict_numeros[numero] = 1
    
    maior = 0
    vezes = 0
    for chave, valor in dict_numeros.items():
        if valor >= vezes:
            vezes = valor
            maior = chave
    return maior

if __name__ == "__main__":

    print (highest_rank(lista = [12, 10, 8, 12, 7, 6, 4, 10, 12,10]))

    num1 = 10
    num2 = 12