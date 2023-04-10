"""
Encapsulamento

É o conceito onde "escondemos" informações internas do objeto, e difinimos as "interfaces"
públicas, onde o usuário terá acesso

"""

class ContaBancaria:
    
    def __init__(self, nome, saldo=0):

        # Criamos 2 atributos privados da classe
        self._nome = nome
        self._saldo = saldo

    def mostar_saldo(self):
        return print(f"O saldo é de {self._saldo}")
    
    def depositar(self, valor):
        self._saldo += valor
        print(f"Deposito de R${valor}")
    def sacar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor 
            print(f"Saque de R${valor}")
            return valor
        
        print(f"Você não possui saldo suficiente para sacar")


if __name__ == "__main__":
    
    conta_corrente_viacred = ContaBancaria("Conta Corrente Viacred", 1000)

    conta_corrente_viacred.mostar_saldo()
    conta_corrente_viacred.depositar(200)
    conta_corrente_viacred.mostar_saldo()
    conta_corrente_viacred.sacar(3000)
    conta_corrente_viacred.mostar_saldo()