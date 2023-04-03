from random import randint

def remove_copias(lista_num):
    lista_num.sort()
    return print(sorted(set(lista_num)))


if __name__ == "__main__":
    
    lista_num = []

    for num in range(50):
        num = randint(0,50)
        lista_num.append(num)

    print(lista_num)
    print("="*50)
    print(remove_copias(lista_num))