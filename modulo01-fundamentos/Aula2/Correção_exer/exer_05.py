from random import randint

if __name__ == "__main__":

    #Utilizando lista comprehension
    lista_numeros = [randint(0, 50) for _ in range(50)]
    # Caso não queiramos utilizar o valor gerado pela função range 
    # Podemos utilizar o _ (underline) para ignorar esse valor 
    # for _ in rage(50)
    #   lista_numero.append(radint(0,50))

    print(f"O maior número desta lista é o {max(lista_numeros)}.")
    print(f"O menor número desta lista é o {min(lista_numeros)}.")