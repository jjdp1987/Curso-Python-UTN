# Creación de un decorador que tenga dos parámetros que limite valores numéricos entre un rango.
# Programa:

def limitar_valores(min_val, max_val):
    """Decorador que asegura que todos los argumentos numéricos estén entre
min_val y max_val."""
    def decorador(func):
        def envoltura(*args, **kwargs):
            for i, arg in enumerate(args):
                if not (arg >=min_val and arg <= max_val):
                     raise ValueError(f"Argumento {arg} en posición {i} fuera del rango [{min_val}, {max_val}]")
            print(f"Todos los argumentos dentro del rango [{min_val}, {max_val}], ejecutando {func.__name__}...")
            return func(*args, **kwargs)
        return envoltura
    return decorador

# Uso del decorador

@limitar_valores(0, 100)
def multiplicar(a, b):
    return a * b

# Llamadas válidas

print(multiplicar(10, 5)) # 50
print(multiplicar(0, 100)) # 0

# Llamada inválida (lanza ValueError)

print(multiplicar(150, 5)) # ValueError