if __name__ == "__main__":
    num = int(input("Informe um número:"))

    if num <= 1:
        print("Você precisa informa um número maior do que 1")
    else:
    
        total = 0
        contador = 1
        while contador <= num:
            total = total + contador
            contador += 1
    
        print(total)