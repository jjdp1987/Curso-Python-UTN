def registrar_argumentos(funcion):
    def envoltura(*args, **kwargs):
        print(f" Llamando a {funcion.__name__}")
        if args:
            print(f" Argumentos posicionales: {args}")
        if kwargs:
            print(f" Argumentos con nombre: {kwargs}")

        resultado = funcion(*args, **kwargs)
        
        print(f" Resultado: {resultado}")
        return resultado
    return envoltura

@registrar_argumentos
def sumar(a, b):
    return a + b

@registrar_argumentos
def saludar_completo(nombre, apellido, formal=False):
    saludo = f"Estimado {nombre} {apellido}" if formal else f"Hola {nombre}"
    return saludo

# Pruebas

sumar(5, 3)
# Llamando a sumar
# Argumentos posicionales: (5, 3)
# Resultado: 8

saludar_completo("Carlos", "López", formal=True)
# Llamando a saludar_completo
# Argumentos posicionales: ('Carlos', 'López')
# Argumentos con nombre: {'formal': True}
# Resultado: Estimado Carlos López