# Creación de un decorador mínimo que muestre un mensaje antes y después de ejecutar la función
# principal.
# Programa:

def mi_primer_decorador(func):
    """
    Este es un decorador básico que imprime un mensaje
    antes y después de la ejecución de la función.
    """
    def envoltura():
        print("Antes de llamar a la función.")
        func() # Llama a la función original que fue pasada a 'mi_primer_decorador'
        print("Después de llamar a la función.")
    return envoltura # Retorna la función 'envoltura'
# Ahora, definimos una función y la "decoramos"
@mi_primer_decorador
def saludar():
 print("¡Hola desde la función saludar!")
# Llamamos a la función decorada
saludar()