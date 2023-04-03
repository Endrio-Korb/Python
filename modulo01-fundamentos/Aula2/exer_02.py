if __name__ == "__main__":

    lista_quadrados = []

    c = True
    while c == True:
        num = int(input("Informe números, informe 0 para parar: "))
        if num == 0:
            break
        lista_quadrados.append(num ** 2)

    print(f"Lista dos quadrados é {lista_quadrados}")
