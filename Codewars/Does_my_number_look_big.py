def narcissistic( value ):
    total = 0
    numeros = []
    for letra in str(value):
        numeros.append(int(letra))

    x = len(numeros)
    for i in numeros:
        total += i ** x
    
    return True if total == value else False



# https://www.codewars.com/kata/5287e858c6b5a9678200083c/train/python

if __name__ == "__main__":

    print(narcissistic(153))