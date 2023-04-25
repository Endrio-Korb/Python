def find_uniq(arr):
    dici = {}
    for iten in arr:
        if dici.get(iten):
            dici[iten] += 1
        else:
            dici[iten] = 1
            
    for chave, valor in dici.items():
        if valor == 1:
            return chave
        
# https://www.codewars.com/kata/585d7d5adb20cf33cb000235


if __name__ == "__main__":

    arr = [ 1, 1, 1, 2, 1, 1 ]
    print(find_uniq(arr))