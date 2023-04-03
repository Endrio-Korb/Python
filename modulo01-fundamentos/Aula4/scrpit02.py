"""
Funções recursivas

Funções recursivos são função que chamam a si mesmas
"""
# Função para calculo de fatorial (n!) ex: 3! = 3 * 2 * 1
def fatorial_nao_recursivo(numero):
    contador = numero
    total = numero

    while contador > 1:
        total *= contador - 1
        contador -= 1
    
    return total

# Função recursiva para calculo de fatorial
def fatorial(numero):
    if numero == 1:
        return numero
    
    return numero * fatorial(numero - 1)

if __name__ == "__main__":
    print(fatorial_nao_recursivo(5))
    print(fatorial(5))