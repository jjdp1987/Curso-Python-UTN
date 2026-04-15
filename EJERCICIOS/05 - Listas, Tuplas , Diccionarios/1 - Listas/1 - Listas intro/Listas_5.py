# Definir una lista por asignación con 5 enteros. Mostrar por pantalla solo los elementos con
# valor iguales o superiores a 7.


lista = [5, 6, 2, 3, 9]

contar = 0

for x in range(len(lista)):
    if lista[x] > 7 or lista[x] == 7:
        contar += 1

print(f"La cantidad de numeros mayores o iguales a 7 es {contar}")