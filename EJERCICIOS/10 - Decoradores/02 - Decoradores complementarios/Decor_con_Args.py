def decorador_correcto(funcion):
    def envoltura(*args, **kwargs): # Acepta cualquier argumento
        print("Antes de ejecutar")
        funcion(*args, **kwargs) # Pasa todos los argumentos
        print("Después de ejecutar")
    return envoltura

@decorador_correcto
def saludar(nombre):
    print(f"Hola {nombre}")

@decorador_correcto
def despedir(nombre, motivo="hasta pronto"):
    print(f"Adiós {nombre}, {motivo}")

# Ahora funciona perfectamente:

saludar("Juan")
# Antes de ejecutar
# Hola Juan
# Después de ejecutar

despedir("María", motivo="nos vemos")
# Antes de ejecutar
# Adiós María, nos vemos
# Después de ejecutar