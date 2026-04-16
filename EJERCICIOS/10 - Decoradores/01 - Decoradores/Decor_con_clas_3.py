# Implementar un decorador de clase con argumentos.
# Programa:

class DecoradorParametrizado:
    def __init__(self, mensaje):
        self.mensaje = mensaje # Guardamos el parámetro del decorador
    def __call__(self, func):
        # Aquí definimos la función envoltura
        def envoltura(*args, **kwargs):
            print(f"{self.mensaje} - Antes de la función")
            resultado = func(*args, **kwargs)
            print(f"{self.mensaje} - Después de la función")
            return resultado
        return envoltura

# Uso del decorador con parámetro @DecoradorParametrizado("Depuración")

def principal():
    print("Función principal ejecutándose.")

# Llamada
principal()