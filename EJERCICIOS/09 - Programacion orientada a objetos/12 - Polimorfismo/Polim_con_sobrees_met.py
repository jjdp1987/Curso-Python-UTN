# Polimorfismo con Sobrescritura de Métodos
# La sobrescritura de métodos es una técnica clave para implementar el polimorfismo. Permite a las
# clases hijas redefinir los métodos de la clase base para proporcionar un comportamiento específico.

class Vehiculo:
    def moverse(self):
        return "El vehículo se mueve."

class Coche(Vehiculo):
    def moverse(self):
        return "El coche está conduciendo."

class Barco(Vehiculo):
    def moverse(self):
        return "El barco está navegando."

# Usar polimorfismo para invocar el método correcto

vehiculos = [Coche(), Barco()]
for vehiculo in vehiculos:
    print(vehiculo.moverse())