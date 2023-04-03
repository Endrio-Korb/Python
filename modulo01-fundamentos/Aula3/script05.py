"""
Funções com argumentos arbitrários

*args
**kwargs

"""

def calculo_media_arbitratio(*args):
    print(f"{sum(args) / len(args):.2f}")

# kw = keyword
def info_usuario(**kwargs):
    print(kwargs)

if __name__ == "__main__":
    
    calculo_media_arbitratio(8,4,5,8,6,5,4)
    calculo_media_arbitratio(5,8,6)

    info_usuario(nome="João", idade = 30)
    info_usuario(nome = "João", data_nascimento = "19770605", sexo = "m" , cidade = "Blumenau")