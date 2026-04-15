#  Desarrollar una funcion que reciba un string como parametro y nos muestre la cantidad de vocales. 
# Llamarla desde el bloque principal del programa 3 veces con string distintos.

def contar_vocales(cadena):
    numero_vocales = 0
    for indice in range(len(cadena)):
        if cadena[indice] == "a" or cadena[indice] == "e" or cadena[indice] == "i" or cadena[indice] == "o" or cadena[indice] == "u":
            numero_vocales += 1
    print(f"El numero de vocales que contiene {cadena} es: {numero_vocales}")

# Bloque principal del programa

contar_vocales("hola")
contar_vocales("administracion")
contar_vocales("abecedario")