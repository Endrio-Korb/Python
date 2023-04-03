from random import randint

if __name__ == "__main__":
    
    contador = 0
    lista_num = []

    while contador <= 5:
        num = randint(0,10)
        contador += 1
        lista_num.append(num)

    print(lista_num)
    lista_num.reverse()
    print(lista_num)