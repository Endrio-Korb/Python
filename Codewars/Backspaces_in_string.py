def clean_string(s):
    lista = []
    saida = ""
    try:
        x = str(s[0])
    except IndexError:
        return ""
    for i in x:
        lista.append(i)
        try:
            if i == '#':
                lista.pop(-1)
                lista.pop(-1)
        except IndexError:
            pass
    if lista == []:
        return saida
    else:
        for letra in lista:
            saida += str(letra)
        return saida


# https://www.codewars.com/kata/5727bb0fe81185ae62000ae3/train/python

if __name__ == "__main__":

    s = ['abc####d##c#']

    print(clean_string(s))