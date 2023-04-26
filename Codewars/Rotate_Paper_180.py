def rotatedDigits(N):
    rotatedDigits = {'0','2','5','6','8','9'}

    lista = []
    rotate = []
    for i in str(n):
        lista.append(i)

    for i in lista:
        for j in rotatedDigits:
            if i == j:
                rotate.append(i)
    
    if lista == rotate:
        return True
    else:
        return False


#https://www.codewars.com/kata/58ad230ce0201e17080001c5/train/python


if __name__ == "__main__":

    n = "88095505522859900269200665822550556088"

    print(rotatedDigits(n))