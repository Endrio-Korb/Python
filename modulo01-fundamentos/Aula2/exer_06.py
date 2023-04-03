if __name__ == "__main__":

    num = int(input("Informe o número de # que deseja imprimir: "))

    contador = 0

    while contador <= num:
        print("#" * contador)
        contador += 1