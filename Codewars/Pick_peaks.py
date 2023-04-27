def pick_peaks(arr):
    d_posicao = {}
    lista_posicao = []
    posicao = 0
    picos = []
    posicoes = []
    anterior = 0
    posterior = 1
    contador = 0
    anterior_ind = 0
    remove = 1
    valores = []
    corte_ind = 0

    x = (arr)

    for i in x:
        try:
            arr.index(i)
            d_posicao.update({posicao:i})
            lista_posicao.append(posicao)
            posicao += 1

        except ValueError:
            pass

    for i in arr:

        if anterior <= i:
            try:
                anterior_ind = (arr.index(i) - 1 )

                if anterior_ind == -1:
                    anterior_ind = 0
                    contador += 1

                if contador >= 2:
                    corte_ind = (arr.index(i) + 1 )
                    arr = arr[corte_ind:]

                anterior_ind = (arr.index(i) - 1)
                
                if anterior_ind == -1:
                    anterior_ind = 0

                anterior = arr[anterior_ind]
                try:
                    posterior_ind = anterior_ind + 2
                    posterior = arr[posterior_ind]
                except IndexError:
                    pass
            except ValueError:
                pass

            if anterior < i and posterior < i:
                picos.append(i)
                for chave, valor in d_posicao.items():

                    if valor == i:
                        posicoes.append(chave)
                        valores.append(valor)

                    if valores.count(valor) > 1:
                        try:
                            posicoes.pop(remove)
                            remove += 1
                        except IndexError:
                            pass
        anterior = 1


    return picos, posicoes


# https://www.codewars.com/kata/5279f6fe5ab7f447890006a7/train/python

if __name__ == "__main__":

    arr = [3,2,3,6,4,1,2,3,2,1,2,3]

    print(pick_peaks(arr))
