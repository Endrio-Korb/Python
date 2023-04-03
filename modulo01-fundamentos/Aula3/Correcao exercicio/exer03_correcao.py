def func(lista):
    # Podemos utilizar sets para eliminar valores repetidos da sequencia
    return list(set(lista))

if __name__ == "__main__":
    lista1 = [1,1,1,1,2,2,2,2,2,3,3,3,3]
    print(func(lista1))