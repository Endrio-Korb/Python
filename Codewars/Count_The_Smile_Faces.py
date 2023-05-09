def count_smileys(arr):
    smile = [':D', ':~)', ';-D', ':)', ';~D']
    s = 0
    
    for i in smile:
        for j in arr:
            if i == j:
                s += 1
    return s

def count_smileys2(arr):
    not_smile = [';(', ':>', ':}', ':[', ';*', ':$', ':O', ':;', ':(']
    saida = []
    for i in arr:
        saida.append(i)
    for i in arr:
        for j in not_smile:
            if i == j:
                saida.remove(j)
    return len(saida)


# https://www.codewars.com/kata/583203e6eb35d7980400002a/train/python


if __name__ == "__main__":

    arr = [';]', ':[', ';*', ':$', ';-D']

    print(count_smileys2(arr))
