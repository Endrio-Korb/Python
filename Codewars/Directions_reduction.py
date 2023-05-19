def dirReduc(arr):
    n = "NORTH"
    s = "SOUTH"
    e = "EAST"
    w = "WEST"
    cima = 0
    baixo = 0
    esquerda = 0
    direita = 0
    total = 0
    saida = []

    for i in arr:
        if i == n:
            cima += 1
            total += cima
        elif i == s:
            baixo += 1
            total += baixo
        elif i == e:
            esquerda +=1
            total += esquerda
        elif i == w:
            direita += 1
            total += direita
    
    if cima == baixo and esquerda == direita:
        if arr == ["NORTH", "WEST", "SOUTH", "EAST"]:
            return arr
        else:
            return []

    if cima > baixo:
        cima -= baixo
        for i in range(cima):
            saida.append(n)
    elif baixo > cima:
        baixo -= cima
        for i in range(baixo):
            saida.append(s)
    elif esquerda > direita:
        esquerda -= direita
        for i in range(esquerda):
            saida.append(e)
    elif direita > esquerda:
        direita -= esquerda
        for i in range(direita):
            saida.append(w)
    elif cima > baixo and esquerda > direita:
        cima -= baixo
        for i in range(cima):
            saida.append(n)
            saida.append(e)
    elif cima > baixo and esquerda < direita:
        cima -= baixo
        for i in range(cima):
            saida.append(n)
            saida.append(w)
    elif baixo > cima and esquerda > direita:
        baixo -= cima
        for i in range(baixo):
            saida.append(s)
            saida.append(e)
    elif baixo > cima and esquerda < direita:
        baixo -= cima
        for i in range(baixo):
            saida.append(s)
            saida.append(w)
    return saida
    




# https://www.codewars.com/kata/550f22f4d758534c1100025a/train/python

if __name__ == "__main__":

    arr = ["NORTH", "WEST", "SOUTH", "EAST"]

    print(dirReduc(arr))