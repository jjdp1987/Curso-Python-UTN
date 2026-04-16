def cache(funcion):
    memoria = {}
    def envoltura(*args):
        if args in memoria:
            print(f"Recuperando de cache: {args}")
            return memoria[args]
        resultado = funcion(*args)
        memoria[args] = resultado
        return resultado
        return envoltura

@cache
def factorial(n):
    if n == 0:
        return 1
        return n * factorial(n-1)
print(factorial(5)) # Calcula
print(factorial(5)) # Usa cache