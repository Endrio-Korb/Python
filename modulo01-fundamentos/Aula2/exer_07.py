if __name__ == "__main__":

    contador = 0
    lista_masculina = []
    lista_feminina = []
    lista_idade = []

    while contador <= 3:
        contador += 1
        nome = input("Infome seu nome: ")
        idade = int(input("Informe sua idade:"))
        sexo = input("Digite [M] para masculino e [F] para feminino:").upper()
        
        if sexo == "M":
            lista_masculina.append(+1)
        elif sexo == "F":
            lista_feminina.append(+1)
        else:
            print("Opção inválida")
            break
        
        lista_idade.append(idade)

        media = sum(lista_idade) / (len(lista_idade))

    print(f"Quantidade de masculino é {len(lista_masculina)}")
    print(f"Quantidade de feminina é {len(lista_feminina)}")
    print(f"A media de idade é de {media}")