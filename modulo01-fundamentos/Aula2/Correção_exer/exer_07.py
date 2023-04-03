if __name__ == "__main__":

    # Criar a lista que ira armazenar as informações
    lista_cliete = []
    qt_masculino = 0
    qt_feminino = 0
    soma_idade = 0

    # Loop que roda 5 vezes
    for _ in range(5):
        
        nome = input("Informe o nome: ")
        idade = int(input("Informe sua idade: "))
        sexo = input("Informe [M] para Masculino e [F] para feminino: ").upper()

        soma_idade = soma_idade = idade

        if sexo == "M":
            qt_masculino = qt_masculino + 1
        elif sexo == "F":
            qt_feminino = qt_feminino + 1
        else:
            print("Valor invalido")

        # Dicionário
        info = {
           #Chave : valor
            "nome" : nome,
            "idade" : idade,
            "sexo" : sexo
        }

        lista_cliete.append(info)

    for cliente in lista_cliete:
        print(f"Nome: {cliente['nome']}")
        print(f"Idade: {cliente['idade']}")
        print(f"Sexo {cliente['sexo']}\n")


    print(f"Quantidade de usuário do sexo masculino {qt_masculino}.")
    print(f"Quantidade de usuário do sexo feminino {qt_feminino}.")
    print(f"Média de idade: {soma_idade / len(lista_cliete):.2f}.")