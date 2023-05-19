def count_with_string(arr):

    resultado = eval(arr[0])

    return resultado

if __name__ == "__main__":

    arr = ["5+5 * (3+2)"]

    print(count_with_string(arr))