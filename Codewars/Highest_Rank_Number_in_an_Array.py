def highest_rank(arr):
    dicio = {}
    maior1 = 0
    saida = []
    
    for numero in arr:
        if dicio.get(numero):
            dicio[numero] += 1
        else:
            dicio[numero] = 1

    for valor in dicio.values():
        if valor > maior1:
            maior1 = valor
        
    for chave, valor in dicio.items():
        if valor == maior1:
            saida.append(chave)

    return max(saida)


# https://www.codewars.com/kata/5420fc9bb5b2c7fd57000004/train/python

if __name__ == "__main__":

    arr = [12, 10, 8, 12, 7, 6, 4, 10, 12, 10]

    print(highest_rank(arr))