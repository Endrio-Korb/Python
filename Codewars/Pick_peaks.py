def pick_peaks(arr):
    d_posicao = {}
    lista_posicao = []
    posicao = 0
    
    picos = []
    posicoes = []
    anterior = 0
    posterior = 1

    for i in arr:
        if anterior <= i:
            try:
                antterior_ind = (arr.index(i) - 1 )
                anterior = arr.[anterior_ind]
                posterior_ind = arr.index(anterior)
                posterior_ind += 2
                posterior = arr[posterior_ind]
            except ValueError:
                pass

            if anterior < i and posterior < i:
                picos.append(i)
                posicoes.append(arr.index(i))






    x = (arr)

    for i in x:
        try:
            arr.index(i)
            d_posicao.update({posicao:i})
            lista_posicao.append(posicao)
            posicao += 1


        except ValueError:
            pass


    
    for chave, valor in d_posicao.items():
        print(f"{chave}: {valor}")





# https://www.codewars.com/kata/5279f6fe5ab7f447890006a7/train/python

if __name__ == "__main__":

    arr = [1,2,3,6,4,1,2,3,2,1]

    print(pick_peaks(arr))
