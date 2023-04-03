if __name__ == "__main__":
    """
    Laçõs de condição em Python -- Laço for
    Utilizamos o laço for quando queremos iterar( ler de forma sequencial) os itens 
    de um container (listas, dicts, etc) e objetos iteráveis (string)

    Exemplos
        - Ler o conteúdo de um arquivo texto
        - Acessar os itens de um resultado de uma chamada ao banco de dados
        - ETC
    """
    lista = [
        "Abacaxi", "Manga", "Limão","Abacate","Tamarindo"
    ]

    jogos = [
        "CG:GO", "GTA V", "Valorant", "LOL", "Arma 2"
    ]

    if __name__ == "__main__":

        for item in lista:
            print(item)

    # Uso do Break
    # Quando temos o comando Break no laço for, o laço é imediatamente interrompido

    #Uso do continue
    # Quanto temos o comando continue o laço for, a interação atual é
    # interrompida, e o loop continua no próximo item

    print("="*30)

    for jogo in jogos:
        if jogo == "Valorant":
            print("Não roda! mas rosa os outros")
            continue
        
        print(jogo)
    # o else no for só funcionará apenas se o loop o for completado e se não for executado
    # o comando break dentro do for
    else:
        print("Executado com sucesso")
