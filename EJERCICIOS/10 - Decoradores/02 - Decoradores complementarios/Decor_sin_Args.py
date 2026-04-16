def decorador_problematico(funcion):
    def envoltura(): # ¡No acepta argumentos!
        print("Antes de ejecutar")
        funcion() # ¡Tampoco pasa argumentos!
        print("Después de ejecutar")
    return envoltura

@decorador_problematico
def saludar(nombre):
    print(f"Hola {nombre}")

# Esto fallaría:
# saludar("Juan") # TypeError: envoltura() takes 0 positional arguments but 1 was given
