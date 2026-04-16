def manejar_errores(funcion):
    def envoltura(*args, **kwargs):
        try:
            resultado = funcion(*args, **kwargs)
            return resultado
        except Exception as e:
            print(f" Error en {funcion.__name__}: {e}")
            return None
    return envoltura
    
@manejar_errores
def dividir(a, b):
    return a / b

@manejar_errores
def obtener_elemento(lista, indice):
    return lista[indice]

print(dividir(10, 2)) # 5.0
print(dividir(10, 0)) # Error en dividir: division by zero, None
lista = [1, 2, 3]
print(obtener_elemento(lista, 1)) # 2
print(obtener_elemento(lista, 10)) # Error en obtener_elemento: list indexout of range, None