# Cargar una oración por teclado. 
# Mostrar luego cuantos espacios en blanco se ingresaron.
# Tener en cuenta que un espacio en blanco es igual a " ", en cambio una cadena vacía es ""

oracion = input("Cargue una oracion: ")

contar_espacio=0

for x in range(len(oracion)):
    if oracion[x] == " ":
        contar_espacio += 1

print("La cantidad de espacios vacios es:", contar_espacio)