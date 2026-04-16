# Plantear una clase dado.
# Programa:

import random

class Dado:
    def __init__(self):
        self.valor = 1
        self.tirar()

    def tirar(self):
        self.valor = random.randint(1, 6)

    def imprimir(self):
        print("El valor del dado es:", self.valor)

dado1 = Dado()
dado1.tirar()
dado1.imprimir()
dado1.valor = 50
dado1.imprimir()