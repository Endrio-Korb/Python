def pick_peaks(arr):
    d_posicao = {}
    lista_posicao = []
    posicao = 0
    
    for i in range(len(arr)):
        try:
            arr.index(i)
            d_posicao.update({posicao:i})
            lista_posicao.append(posicao)
            posicao += 1
            arr.remove(i)

        except ValueError:
            pass


    
    for chave, valor in d_posicao.items():
        print(f"{chave}: {valor}")





# https://www.codewars.com/kata/5279f6fe5ab7f447890006a7/train/python

if __name__ == "__main__":

    arr = [1,2,3,6,4,1,2,3,2,1]

    print(pick_peaks(arr))
