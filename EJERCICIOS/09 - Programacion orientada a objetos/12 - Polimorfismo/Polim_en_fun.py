# Polimorfismo en Funciones
# El polimorfismo también puede aparecer en funciones que aceptan diferentes tipos de datos.
# Python, al ser un lenguaje dinámico, no exige declarar el tipo de los parámetros en las funciones, lo
# que permite que estas funciones sean polimórficas de manera implícita.
# Ejemplo de Polimorfismo en Funciones

def sumar(a, b):
    return a + b

# Usar la función con diferentes tipos de datos

print(sumar(5, 3)) # Funciona con enteros (Imprime 8)
print(sumar(2.5, 4.5)) # Funciona con flotantes (Imprime 7.0)
print(sumar("Hola, ", "Mundo!")) # Funciona con cadenas (Imprime "Hola, Mundo!")