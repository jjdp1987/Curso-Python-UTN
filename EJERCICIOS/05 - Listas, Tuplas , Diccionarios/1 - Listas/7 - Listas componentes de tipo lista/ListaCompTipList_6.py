# Crear una lista por asignación con la cantidad de elementos de tipo lista que usted desee.
# Luego imprimir el último elemento de la lista principal.

lista = [["Manzana", "Pera"], [10, 20, 30], ["Lunes", "Martes", "Miércoles"]]

print("Lista completa:")
print(lista)

print("\nEl último elemento (usando índice -1) es:")
print(lista[-1])

print("\nEl último elemento (usando len-1) es:")
ultimo_indice = len(lista) - 1
print(lista[ultimo_indice])