from random import randint

if __name__ == "__main__":
    
    contador = 1

    lista_par = []
    lista_impar = []

    while contador <= 100:
        num = randint(1, 100)
        contador += 1

        if num % 2 == 0:
            lista_par.append(num)
        else:
            lista_impar.append(num)

    print(f"Quantidade de números pares é de {len(lista_par)}")
    print(f"Valores: {lista_par}")

    print(f"Quantidade de números impares é de {len(lista_impar)}")
    print(f"Valores: {lista_impar}")