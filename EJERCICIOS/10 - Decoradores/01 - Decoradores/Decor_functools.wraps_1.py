def mi_decorador(func):
    def envoltura(*args, **kwargs):
        """Función envoltorio sin docstring de la original"""
        print("Antes de la función...")
        resultado = func(*args, **kwargs)
        print("Después de la función...")
        return resultado
    return envoltura
@mi_decorador
def saludar():
    """Esta función imprime un saludo amigable."""
    print("¡Hola!")
print(saludar.__name__) # envoltura
print(saludar.__doc__) # Función envoltorio sin docstring de la original