# Se tiene la siguiente lista:
# lista=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]
# Imprimir la lista. Luego fijar con el valor cero todos los elementos mayores a 50 del primer elemento de "lista".
# Volver a imprimir la lista. 

# Definición de la lista de listas original
lista = [[100, 7, 85, 8], [4, 8, 56, 25], [67, 89, 23, 1], [78, 56]]

# 1. Imprimir la lista original
print("Lista original:")
print(lista)

# 2. Fijar con el valor cero los elementos mayores a 50 
# únicamente de la PRIMERA sublista (índice 0)
for x in range(len(lista[0])):
    if lista[0][x] > 50:
        lista[0][x] = 0

# 3. Volver a imprimir la lista modificada
print("\nLista modificada (mayores a 50 del primer elemento en cero):")
print(lista)