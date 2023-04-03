"""
Funções

Fução é um bloco de código que pode ser reutilizado em quiasquer
lugares do nosso código
Em python utilizamos a palavra def para criar funções

"""

def hello():
    print("Olá")

def randomico():
    return 1

if __name__ == "__main__":
    
    # Para executar a função simplesmente a chamamos
    # Função são objetos chamáveis (callable)
    # Como não utilizamos o return dentro da função hello 
    # por padrão essa função vai retornar um valor None
    hello()
    print(hello())
    print(randomico())

    # Nesse caso, a função randomico() retorna um valor
    # que é salvo em uma variável
    valor = randomico()
    print(valor)