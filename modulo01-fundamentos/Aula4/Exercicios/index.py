def pyramid(n):
    piramid = []
    contador2 = 0
    contador1 = n[0]
    contador3 = n[0]
    c = True
    
    if contador1 == []:
        return contador1
    else:
        while c == True:
            for i in range(contador2):
                piramid.append([1])
        
            contador2 += 1
            for i in range(1):
                if contador1 == 1:
                    contador3 == 1
                else:
                    contador3 -= 1
        return piramid

if __name__ == "__main__":
     n = [1]
     print(pyramid(n))