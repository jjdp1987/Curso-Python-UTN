# Ingresar una oración que pueden tener letras tanto en mayúsculas como minúsculas. 
# Contar la cantidad de vocales. 
# Crear un segundo string con toda la oración en minúsculas para que sea más fácil 
# disponer la condición que verifica que es una vocal.

oracion = input("Ingrese una oracion: ")

oracion_min = oracion.lower()
contar_vocales=0

for x in range(len(oracion)):
    if oracion_min[x] == "a" or oracion_min[x] == "e" or oracion_min[x] == "i" or oracion_min[x] == "o" or oracion_min[x] == "u":
        contar_vocales += 1

print("La cantidad de vocales es:", contar_vocales)