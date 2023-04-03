from random import randint

if __name__ == "__main__":

    contador = 0
    lista_num = []

    while contador <= 20:
        contador += 1
        num = randint(0,50)
        lista_num.append(num)
    
    lista_num.sort()
    print(lista_num)
   
    print("="*30)
    print(sorted(set(lista_num)))