from random import randint

if __name__ == "__main__":
    
    contador = 0
    lista_num = []
    
    while contador <= 10:
        contador += 1
        num = randint(0,50)
        lista_num.append(num)
    
    lista_num.sort()

    print(lista_num)
    print(f"O maior valor da lista é {max(lista_num)}")
    print(f"O menor valor da lista é {min(lista_num)}")