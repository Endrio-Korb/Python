# Cálculo de média de 3 notas

"""
O script irá receber 3 notas via linha de comando. As regras do cálculo serão as seguintes:

Se a média for menor do que 5 o aluno estará reprovado
Se a média for mair ou igual a 5 e menor do que 7 o aluno estará de recuperação
Se a média for maior ou igual a 7 o aluno estará aprovado
"""
if __name__ == "__main__":
    nota1 = float(input("Insira a nota 1 :"))
    nota2 = float(input("Insira a nota 2 :"))
    nota3 = float(input("Insira a nota 3: "))

    media = (nota1 + nota2 + nota3) / 3



    # {:.2f}".format(media) serve para limitar a quantidade de casas após a virgula que será mostrada
    if media < 5:
        print("O aluno está reprovado com a média {:.2f}".format(media))

        # Também pode  ser usado elif media >= 5 and media <7 :
    elif media < 7:
        print("O aluno está de recuperação com a média {:.2f}".format(media))
    elif media >=7 and media <=10:
        print("O aluno está aprovado com a média {:.2f}".format(media))
    else:
        print("Valores de notas inválidos, favor inserir novamente")