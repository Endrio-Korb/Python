if __name__ == "__main__":

    nota1 = float(input("Informe a nota 1:"))
    nota2 = float(input("Informe a nota 2:"))
    nota3 = float(input("Informe a nota 3:"))
    nota4 = float(input("Informe a nota 4:"))
    nota5 = float(input("Informe a nota 5:"))

    """
    Podemos criar lista de duas maneiras:
    lista = list()
    lista = []
    """

    "Também podemos criar a lista já com os valores"
    lista_nota = [nota1, nota2, nota3, nota4, nota5]

    # O metodo append insere um item sempre no fianl da lista
    #lista_nota.append(nota1)
 
    #A função .sort ordena por padrão os números do menor para maior e letras em ordem alfabética
    lista_nota.sort()

    #Podemos remover os itens usando a função .pop
    #lista_nota.pop(0)

    # Quando não souber o tamnho da lista e quiser remover o último item pode usar o valor -1, por que no Python
    # ele permite números negativos na lista

    #lista_nota.pop(-1)

    # Método slice -> fatiamento da lista
    # Passamos o indice inicial e um índice final do que queremos extrair
    # Neste caso é gerada uma lista nova
    lista_nota = lista_nota[1:4]

    # len() é uma função Built-in que retorna a quantidade de intens de 
    # um iterator ( no nosso caso a lista de notas)
    # som() é uma função Built-in que retornar a soma dos números de um 
    # container que no nossa caso é as notas
    media = sum(lista_nota) / len(lista_nota)

    print(f"A média foi de {media:.2f}")