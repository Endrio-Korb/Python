from random import randint

if __name__ == "__main__":

    lista_randomicos = [randint(1,50) for _ in range(50)]
    lista_numeros = []

    lista_randomicos.sort()

    for numero in lista_randomicos:
        # Se o número não estiver na lista números adiciona nela
        if numero not in lista_numeros:
            lista_numeros.append(numero)
    
    print(lista_randomicos)
    print("=" * 30)
    print(lista_numeros)
    print("=" * 30)
    #Podemos fazer a mesma coisa utilizando a função set, pois esse tipo de
    # dado não permite valores repetidos
    print(list(set(lista_randomicos)))

