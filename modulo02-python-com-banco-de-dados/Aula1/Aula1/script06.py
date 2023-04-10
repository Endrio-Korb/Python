"""
Composição

Composição é quando uma classe compõe ou é composta por outras classes

"""

class Baralho:

    # Quando queremos cirar um objeto que seja iterável, precisamos impletar 2 métodos mágicos __iter__, __next__
    # o método __iter__ por padrão, retorna o própio objeto
    def __iter__(self):
        return self

     # Implementando o método mágica __len__, podemos passar o objeto dessa classe para a função built-in len()
    def __len__(self):
        return len(self._lista_de_cartas)

    # O método __next__ coném a lógica de iteração das classes
    def __next__(self):
        if self._indice >= len(self._lista_de_cartas):
            raise StopIteration
        
        carta = self._lista_de_cartas[self._indice]
        self._indice += 1
        return carta


    def __init__(self):

        self._indice = 0
        # Lista que irá armazenar os objetos do tipo Carta
        self._lista_de_cartas = []

        # Lista auxiliar que será usada para criar os bojetos do tipo Carta
        self._valores = ["2", "3", "4","5","6",
        "7","8","9","10","Q","J","K","A"]

        # Lista auxiluar que será usada para criar os objetor do tipo Carta
        self._naipes = ["\u2660","\u2665","\u2666","\u2663"]

        # Chama o método para construir o baralho
        self._construir_baralho()



    def _construir_baralho(self):
        for valor in self._valores:
            for naipe in self._naipes:
                self._lista_de_cartas.append(Carta(naipe,valor))


class Carta:
    def __init__(self, naipe, valor):
        self._naipe = naipe
        self._valor = valor


    def __repr__(self):
        return f"Carta {self._valor}{self._naipe}"


    def __str__(self):
        return f"Carta {self._valor}{self._naipe}"

    


if __name__ == "__main__":
    
    baralho = Baralho()
    #print(baralho._lista_de_cartas)
    print(f"O Baralho possui {len(baralho)} cartas")
    for carta in baralho:
        print(carta)