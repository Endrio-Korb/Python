def highest_rank(arr):
    dicio = {}
    
    for numero in arr:
        if dicio.get(numero):
            dicio[numero] += 1
        else:
            dicio[numero] = 1
    
    num1 = 0
    num2 = 0
    vezes = 0
    for chave, valor in dicio.items():
        if valor >= vezes:
            vezes = valor
            num1 = chave
    
    maior2 = 0
    
    for i in dicio:
        if i > maior2:
            maior2 = i
            num2 = i


    if num2 >= num1 and maior2 < vezes:
        return num2
    elif num1 <= num2 and vezes < maior2:
        return num1



# https://www.codewars.com/kata/5420fc9bb5b2c7fd57000004/train/python


if __name__ == "_main__":

    arr = [12, 10, 8, 12, 7, 6, 4, 10, 12]

    print(highest_rank(arr))