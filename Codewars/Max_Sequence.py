def max_sequence(arr):
    saida = 0
    for item in arr:
        saida += item

    return 0 if saida <= 0 else saida


if __name__ == "__main__":

    arr = [7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]

    print(max_sequence(arr))