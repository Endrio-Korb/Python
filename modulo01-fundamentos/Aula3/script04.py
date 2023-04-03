"""
Funções

Parâmetros são valores que podemos passar para "dentro" das funções
Argumentos = Parâmetros
Parâmetros = Argumentos
"""
# Definimos os parâmetros dentro dos parêntesis na declaração da função
def calculo_imc(peso, altura):
    imc = peso / ( altura ** 2 )
    return imc

# O argumento tipo_funcionario é um argumento com o valor padrão
# Se não for informado um valor para esse parâmetro, ele assume o valor padrão
def calculo_salario(nome, tipo_funcionario=1):
    if tipo_funcionario == 1:
        print(f"O salário de {nome} é 1000")
    else:
       print(f"O salário de {nome} é 2000")

if __name__ == "__main__":
    
    # Chamamos a função chamando os argumentos da maneira posicional
    imc = calculo_imc(60, 1.75)
    print(imc)

    # Chamamos a função indicando os argumentos pelo nome
    imc = calculo_imc(altura = 2.10, peso = 121)

    dados_usuario = {
        "altura":1.79,
        "peso":98
    }

    print(calculo_imc(**dados_usuario))
    # calculo_imc(altura=1.79, peso=90)

    nome = "João"
    calculo_salario(nome)