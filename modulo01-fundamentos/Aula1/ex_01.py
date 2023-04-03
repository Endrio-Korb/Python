"""
Desenvolver um script de cálculo de comissão de vendas


O vendedor terá um salário fixo de R$ 1000,00. Dependendo do valor vendido no mês, o funcionário
receberá uma comissão de x%. Esse valor vendido será recebido pelo terminal: 
Regras:
Se o funcinário menos de R$ 10000,00, não recebe comissão
Se o funcinário entre de R$ 10000,00 e menos que R$ 50000,00, receberá 10% de comissão
Se o funcinário entre de R$ 50000,00 e menos que R$ 200000,00, receberá 20% de comissão
Se o funcinário acima de R$ 200000,00 receberá 30% de comissão

No final será mostrado o valor fixo + comissão
"""
if __name__ == "__main__":

    SB = 1000

    venda = float(input("Insira o valor de venda:"))

    if venda < 10000:
        print(f"O funcionário não receberá comissão e o valor recebido é de R${SB}")

    elif venda >= 10000 and venda <50000:
        com = (venda * 0.1) + SB
        sl= com + SB
        print(f"O valor da comissão é de 10% e receberá {SB:.2f} mais comissão de:{com:.2f} no total será {sl:.2f}")

    elif venda >=50000 and venda <200000:
        com = (venda * 0.2) + SB
        sl= com + SB
        print(f"O valor da comissão é de 20% e receberá {SB:.2f} mais comissão de {com:.2f} no total será {sl:.2f}:")

    else:
        com = (venda * 0.3) + SB
        sl= com + SB
        print(f"O valor da comissão é de 30% e receberá {SB:.2f} mais comissão de {com:.2f} no total será {sl:.2f}:")