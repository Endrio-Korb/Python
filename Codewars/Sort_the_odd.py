def sort_array(source_array):
    lista_impar = []
    lista_posicao = []
    posicao_valor = {}

    for i in source_array:
        if (i % 2) != 0:
            lista_impar.append(i)
            posicao = source_array.index(i)
            lista_posicao.append(posicao)
    
    x = len(lista_impar)
    lista_impar = sorted(lista_impar)
    posicao = 0
    numero = 0
    for i in range(x):
        lugar = lista_posicao[posicao]
        impar = lista_impar[numero]
        posicao_valor.update({lugar: impar})
        posicao += 1
        numero += 1

    for posicao, numero in posicao_valor.items():
        source_array.pop(posicao)
        source_array.insert(posicao, numero)

    return source_array

    



if __name__ == "__main__":

    source_array = [-34, -22, -35, -29, -13, 2, 20, -11, -7, -16, -7, 3, -26, 7, 46, 11, 17, 19, 25, 27, 14, 31, 42, 33, 45, 24, -20]

    print(sort_array(source_array))
