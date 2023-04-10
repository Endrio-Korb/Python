"""
Herença

Herença acontece quando uma classe herda atributos e caracteristicas de uma classe mão 
ou superclasse

"""
from Excecoes import SaldoInsucienteError


class ContaFinanceira:
    
    def __init__(self,nome, saldo=0):
        self._nome = nome
        self._saldo = saldo

    def mostar_saldo(self):
        print(f"O saldo atual da conta {self._nome} é de R${self._saldo:.2f}")

    def sacar(self):
        raise NotImplementedError

    def depositar(self):
        raise NotImplementedError
    
    def transferir(self ):
        raise NotImplementedError


# Quando queremos indicar a classe a qual será herdada, indiciamos seu nome entre parenteses
# No caso abaixo indicamos que a classe ContaCorrente herda de ContaFinanciera
class ContaCorrente(ContaFinanceira):
    def sacar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
            return valor
        else:
            raise SaldoInsucienteError

    def depositar(self, valor):
        self._saldo += valor
    
    def transferir(self,conta, valor):
        pass
        

class ContaInvestimento(ContaFinanceira):

    def __init__(self, nome, saldo=0, taxa=0.01):
        self._taxa = taxa
        super().__init__(nome=nome,saldo=saldo)

    def render(self):
       # self._saldo = self._saldo + (self._saldo * self._taxa) 
       # O código acima é a mesma coisa que o código abaixo  
       self._saldo += (self._saldo * self._taxa)


if __name__ == "__main__":
    
    try:
        conta = ContaCorrente("Endrio", 1000)
        conta.sacar(100)

        conta_poupanca = ContaInvestimento("Poupança Caixa", 1000)
        conta_poupanca.mostar_saldo()
        conta_poupanca.render()
        conta_poupanca.mostar_saldo()

    except Exception as exc:
        print(exc)