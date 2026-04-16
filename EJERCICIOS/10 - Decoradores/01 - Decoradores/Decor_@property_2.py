# Plantear una clase dado. Ocultar el atributo que almacena el valor del dado y exponerlo a través de
# una propiedad.
# Programa:

import random

class Dado:
    def __init__(self):
        self._valor = 1

    def tirar(self):
        self.valor = random.randint(1, 6)

    @property
    def valor(self):
        return self._valor
    
    @valor.setter
    def valor(self, nuevo_valor):
        if nuevo_valor >=1 and nuevo_valor <= 6:
            self._valor = nuevo_valor
        else:
            raise ValueError("Error: El valor del dado debe estar entre 1 y 6.")

dado1 = Dado()
dado1.tirar()
print("Valor del dado",dado1.valor)
dado1.valor = 3
print("Valor del dado",dado1.valor)
dado1.valor = 50 # Esto genera un error