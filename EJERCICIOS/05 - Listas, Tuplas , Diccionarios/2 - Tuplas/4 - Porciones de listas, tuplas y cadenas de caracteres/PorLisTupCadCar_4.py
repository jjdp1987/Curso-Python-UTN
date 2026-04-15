# Cargar una cadena por teclado luego:
# 1) Imprimir los dos primeros caracteres.
# 2) Imprimir los dos últimos
# 3) Imprimir todos menos el primero y el último caracter.

cadena=input("Ingrese una cadena de caracteres:")
print("Los dos primeros caracteres")
print(cadena[:2])
print("Los dos ultimos caracteres")
print(cadena[len(cadena)-2:])
print("Todos los caracteres menos el primero y el ultimo")
print(cadena[1:len(cadena)-1])