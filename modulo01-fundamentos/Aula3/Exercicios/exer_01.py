def soma_valores(*args):
    return (sum(lista_num))

if __name__ == "__main__":

    lista_num = []
    while True:
        num = int(input("Informe número para somar e pressione [0] para sair: "))
        lista_num.append(num)
        if num == 0:
            break
    
    print(soma_valores())
    