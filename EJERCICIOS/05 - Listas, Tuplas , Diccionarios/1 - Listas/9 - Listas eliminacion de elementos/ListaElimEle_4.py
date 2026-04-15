# Crear una lista de 5 enteros y cargarlos por teclado. 
# Borrar los elementos mayores o iguales a 10 y generar una nueva lista con dichos valores.

# 1. Crear y cargar la lista de 5 enteros por teclado
lista_original = []
for x in range(5):
    valor = int(input("Ingrese un valor entero: "))
    lista_original.append(valor)

print("\nLista inicial:", lista_original)

# 2. Definir la nueva lista donde moveremos los valores >= 10
lista_mayores = []

# 3. Recorrer la lista original para filtrar los datos
posicion = 0
while posicion < len(lista_original):
    if lista_original[posicion] >= 10:
        # Si el valor es >= 10, lo agregamos a la nueva lista
        lista_mayores.append(lista_original[posicion])
        # Lo borramos de la lista original
        lista_original.pop(posicion)
        # NO incrementamos posicion porque el siguiente elemento se desplazó al índice actual
    else:
        # Si es menor a 10, lo dejamos y pasamos al siguiente
        posicion = posicion + 1

# 4. Mostrar los resultados finales
print("Lista original (quedaron los menores a 10):", lista_original)
print("Nueva lista (con los valores mayores o iguales a 10):", lista_mayores) 