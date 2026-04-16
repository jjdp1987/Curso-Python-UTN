import functools

def mi_decorador(func):
    @functools.wraps(func)
    def envoltura(*args, **kwargs):
        """Función envoltorio"""
        print("Antes de la función...")
        resultado = func(*args, **kwargs)
        print("Después de la función...")
        return resultado
    return envoltura
@mi_decorador

def saludar():
    """Esta función imprime un saludo amigable."""
    print("¡Hola!")
print(saludar.__name__) # saludar
print(saludar.__doc__) # Esta función imprime un saludo amigable.
