def pick_peaks(arr):
    d_posicao = {}
    posicao = 0
    picos = []
    posicoes = []
    anterior = 0
    posterior = 1
    anterior_ind = 0
    x = []

    x = arr

    for i in x:
        try:
            arr.index(i)
            d_posicao.update({posicao:i})
            posicao += 1

        except ValueError:
            pass

        for chave, valor in d_posicao.items():
            try:
                anterior_ind = chave -1
                posterior_ind = chave + 1
                if anterior == -1:
                    return IndexError
                if valor == i:
                    anterior = x[anterior_ind]
                    posterior = x[posterior_ind]
                if valor > anterior and valor > posterior:
                    posicoes.append(chave)
                    picos.append(valor)

            except IndexError:
                pass

    return {'pos': posicoes, 'peaks': picos}


# https://www.codewars.com/kata/5279f6fe5ab7f447890006a7/train/python


if __name__ == "__main__":

    arr = [3,2,3,6,4,1,2,3,2,1,2,3]

    print(pick_peaks(arr))
