def duplicate_count(text):
    dici = {}
    saida = []
    numero_itens = []

    try:
        copia = str(text[0])

        for letra in copia:
            if dici.get(letra):
                dici[letra]+= 1
            else:
                dici[letra] = 1

        for valor in dici.values():
            if valor > 1:
                numero_itens.append(valor)

        saida = len(numero_itens)

        return saida
    
    except IndexError:
        return 0



if __name__ == "__main__":

    text = ["Indivisibilities"]

    print(duplicate_count(text))