"""
Dicionários são estruturas que armazenam dados no formato chave-valor.
Dicionários são indexáveis, iteráveis,modificaveis e que não permite 
chaves duplicadas
"""

if __name__ == "__main__":
    
    # Podemos criar dicionários de duas maneiras: Diretamente e 
    # utilizando a função built-in dict()

    # Forma direta
    cliente = {
        "nome": "maria",
        "idade": 30,
        "status": "inativa"
    }

    # Utilizando a função built-in dict()
    # Os parâmetros da função o serão as chaves, e os valores serão os valores
    # serão associoados as chaves
    cliente = dict(nome="José", idade = 28, status = "Ativo")
    print(cliente)

    # Como os dicionários são indexáveis, utilzamos o nome da chave
    # para acessar o seu valor
    print(cliente["idade"])

    # Os dicionários também são iteráveis, ou seja, conseguimos acessar
    # os itens de maneira sequencial

    # Por padrão "cliete:" ira imprimir as chaves que seria o mesmo que cliente.keys()
    # Para imprimir os valores podemos usar o cliente.values()
    for item in cliente.values():
        print(item)

    # Se quisermos pegar tanto chave quanto valor do dicionário,
    # temos que utilizar o método items()
    for item in cliente.items():
        print(item)

    # Ao criar um dicionário baseado em um já existente, temos o mesmo problema
    # de cópia de lista. Precisamos utilizar o método copy() cirar uma cópia do 
    # dicionário e salvar em outro
    dict2 = cliente
    dict2["status"] = "Inativo"
    print(cliente)
    print(dict2)
    