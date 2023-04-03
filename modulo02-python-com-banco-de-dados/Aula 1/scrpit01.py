"""
Progamaçã Orientada a Objeto em Python

Classes, objetos, atributos e métodos

"""

# Utilizamos a palavra reservadas class para criar uma classe

# Em Python, geralmente utilizamos a sintaxe PascalCase para definir os nomes
# das nossas classes
class Pokemon:
    
    # O método __init__ é o um método inicializador da classe ( alguns aceitam o termo método construtor)
    # O método __init__ é chamado sempre que uma classe é instanciada
    # Os métodos funcionam como funções comuns em Python, a difrença é que, sendo um petodo de instânia
    # da classe, eles SEMPRE reebem como primeiro argumento o "self"
    def __init__(self,name, type, health):

        # Como não temos o conceito de privado em Python, quando queremos indicar que um atributo ou método
        # não pode ser acessado diretamente, colocamos um underline na frente do nome.
        self._name = name
        self._type = type
        self.health = health

    def attack(self):
        print(f"{self._name} atacou!")
    
    def dodge(self):
        print(f"{self._name} desviou!")
    
    def evolve(self):
        print(f"{self._name} evoluiu!")


if __name__ == "__main__":
    
    # A linha abaixo instancia um obketo do tipo Pokemon
    pikachu  = Pokemon(name = "Pikachu", type = "Elétrico", health = 70)
    print(pikachu)

    # Dessa maneira chamamos os métodos
    pikachu.attack()
    pikachu.evolve()
    pikachu.dodge()