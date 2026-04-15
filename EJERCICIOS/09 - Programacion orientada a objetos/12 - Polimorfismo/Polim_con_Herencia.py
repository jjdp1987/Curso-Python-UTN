# Ejemplo de Polimorfismo con Herencia

class Animal:
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau!"
# Función que acepta objetos de diferentes clases

def reproducir_sonido(animal):
    print(animal.hacer_sonido())

# Uso de la función

perro = Perro()
gato = Gato()
reproducir_sonido(perro) # Imprime "Guau!"
reproducir_sonido(gato) # Imprime "Miau!"

# Explicación:
# • En este ejemplo, tenemos una clase base Animal que define el método
# hacer_sonido(). Las clases hijas (Perro y Gato) sobrescriben ese método para
# implementar sus propios sonidos.
# • La función reproducir_sonido() es polimórfica porque puede aceptar cualquier
# objeto que implemente el método hacer_sonido(), independientemente de la clase
# específica.