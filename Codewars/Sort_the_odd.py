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


# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python


if __name__ == "__main__":

    source_array = [1, 1, 5, 11, 2, 11, 111, 0]

    print(sort_array(source_array))
