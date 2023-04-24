def find_uniq(arr):
    dici = {}
    saida = []
    for iten in arr:
        if dici.get(iten):
            dici[iten] += 1
        else:
            dici[iten] = 1
            
    for chave, valor in dici.items():
        if valor == 1:
            return chave
        

if __name__ == "__main__":

    arr = [ 1, 1, 1, 2, 1, 1 ]
    print(find_uniq(arr))