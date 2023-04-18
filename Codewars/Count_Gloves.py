def number_of_pairs(gloves):
    pares = 0
    dic = dict()
    for palavra in gloves:
        if palavra in dic:
            dic[palavra] = dic[palavra] + 1
        else:
            dic[palavra] = 1

    for valor in dic.values():
        if (valor % 2) != 0:
            num = valor - 1
        else:
            num = valor
        if num == 0:
            pass
        else:
            if num > 2:
                value = 2
                num = num / 2
                for i in range(int(num)):
                    if num % 2 == 0:
                        pares += value
            else:
                if (num % 2) == 0:
                    pares +=1
                else:
                    if (valor % 2) == 0:
                        pares += 1
        
    return pares

def number_of_pais2(gloves):
    return sum(gloves.count(color)//2 for color in set(gloves))

if __name__ == "__main__":
     

    gloves = ['White', 'Silver', 'Blue', 'Fuchsia', 'White', 'Yellow', 'Purple', 'Gray', 'Gray', 'Red', 'Lime', 'Maroon', 'Aqua', 'Red', 'Green', 'Lime', 'Navy', 'Fuchsia', 'Green', 'Fuchsia', 'Red', 'Silver', 'White', 'White']
    #print(number_of_pairs(gloves))

    # Another way to do this
    print(number_of_pais2(gloves))