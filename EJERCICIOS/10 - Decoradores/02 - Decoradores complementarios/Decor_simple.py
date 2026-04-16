def decorador_saludo(funcion):
    def envoltura():
        print("¡Hola! Antes de ejecutar la función")
        funcion()
        print("¡Adiós! Después de ejecutar la función")
    return envoltura

@decorador_saludo
def saludar():
    print("Estoy saludando desde la función principal")
saludar()