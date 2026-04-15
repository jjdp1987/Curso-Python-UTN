# Definir por asignación una lista con 8 elementos enteros. Contar cuantos de dichos valores
# almacenan un valor superior a 100.

lista = [5, 85, 523, 856, 25, 63, 120, 85]

contar = 0

for x in range(len(lista)):
    if lista[x] > 100:
        contar += 1

print(f"La cantidad de numeros mayores a 100 es {contar}")