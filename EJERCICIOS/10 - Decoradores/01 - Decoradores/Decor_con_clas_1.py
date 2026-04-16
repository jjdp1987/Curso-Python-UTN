# Creación de un decorador mínimo utilizando decorador de clase.
# Programa:

class MiPrimerDecorador:
    """
    Este decorador imprime un mensaje antes y después
    de ejecutar la función, usando __call__.
    """
    def __init__(self, func):
        self.func = func # Guardamos la función original
    def __call__(self):
        print("Antes de llamar a la función.")
        self.func() # Llamamos a la función original
        print("Después de llamar a la función.")

# Ahora, definimos la función y la decoramos usando la clase @MiPrimerDecorador

def saludar():
    print("¡Hola desde la función saludar!")

# Llamamos a la función decorada

saludar()