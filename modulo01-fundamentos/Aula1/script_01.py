    # Entrada e saída em Python no terminal

    # Isso é um comentário

    # A linha abaixo indicas que este script será chamado primeiro na nossa aplicação
    # Apesar de não ser obrigatório, é considerado boa prática.
if __name__ == "__main__":
    # A função print rece um tipo de dado (string, numero, objeto, etc)
    # Exibe no terminal
    #print("Olá mundo.")

    # A função input espera uma informação ser digitada pelo teclado e retorna este valor
    # A função input() pode receber um argumento não obrigatório prompt, que será o texto exibido para o usário

    nome = input("Informe seu nome: ")
    
    # A função input retorna uma string com a informação que veio do teclado

    #print("Bem vindo " + nome)
    print(f"Bem vindo {nome}")

    # Stings é o tipo de dado em Python que representa uma cadeia de caracteres.
    # É considerado string qualquer coisa que estiver dentro de aspas duplas ("") 
    # ou asplas simples ('')

    num1 = int(input("Informe um número:"))
    num2 = input("Informe o segundo número: ")

    soma = num1 + int(num2)

    # f-string são strings onde podemos substituir os valores que estão dentro de chaves
    # por qualquer expressão válidade em Python
  
    print(f"A soma dos valores {num1} e {num2} é igual a {soma}")

    # Expressão em Python são consjuntos de operadores e opernados que resolvem para 
    # um único valor

    num3 = 8 + (3 ** 3) / 5 - (14 * 5) + 0
    print(num3)