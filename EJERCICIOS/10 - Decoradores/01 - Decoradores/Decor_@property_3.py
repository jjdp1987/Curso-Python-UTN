# Crear la clase Cuadrado con dos propiedades derivadas: superficie y perimetro
# Programa:

class Cuadrado:
    def __init__(self, lado):
        self._lado = lado # atributo interno

    @property
    def lado(self):
        return self._lado

    @lado.setter
    def lado(self, nuevo_lado):
        if nuevo_lado > 0:
            self._lado = nuevo_lado
        else:
            raise ValueError("El lado debe ser mayor que 0")

    @property
    def superficie(self):
        """Propiedad derivada: calcula el área del cuadrado"""
        return self._lado ** 2

    @property
    def perimetro(self):
        """Propiedad derivada: calcula el perímetro del cuadrado"""
        return 4 * self._lado

c = Cuadrado(5)
print("Lado:", c.lado)
print("Superficie:", c.superficie) # 25
print("Perímetro:", c.perimetro) # 20
c.lado = 10
print("Nuevo lado:", c.lado)
print("Superficie:", c.superficie) # 100
print("Perímetro:", c.perimetro) # 40
