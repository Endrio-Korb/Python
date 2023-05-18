
def count_with_string(arr):
    numeros = [x for x in arr[0]]
    index1 = numeros.index('(') + 1
    index2 = numeros.index(')') - 1
    operadores = ['+', '-', '*', '/']
    parenteses = 0
    calculo1 = 0
    remover = index1 - 1


    if '+' == numeros[index1 + 1]:
        parenteses = int(numeros[index1]) + int(numeros[index2])
    elif '-' == numeros[index1 + 1]:
        parenteses = int(numeros[index1]) - int(numeros[index2])
    elif '/' == numeros[index1 + 1]:
        parenteses = int(numeros[index1]) / int(numeros[index2])
    elif '*' == numeros[index1 + 1]:
        parenteses = int(numeros[index1]) * int(numeros[index2])

    numeros = numeros[:remover]

    if numeros[1] == '+':
        index = numeros.index('+')
        calculo1 = int(numeros[index - 1]) + int(numeros[index + 1])
        numeros = numeros[index + 2:]
    elif numeros[1] == '-':
        index = numeros.index('-')
        calculo1 = int(numeros[index - 1]) - int(numeros[index + 1])
        numeros = numeros[index + 2:]
    elif numeros[1] == '*':
        index = numeros.index('*')
        calculo1 = int(numeros[index - 1]) * int(numeros[index + 1])
        numeros = numeros[index + 2:]
    elif numeros[1] == '/':
        index = numeros.index('/')
        calculo1 = int(numeros[index - 1]) / int(numeros[index + 1])
        numeros = numeros[index + 2:]


    return calculo1 * parenteses   



if __name__ == "__main__":

    arr = ["5+5(3+2)"]

    print(count_with_string(arr))