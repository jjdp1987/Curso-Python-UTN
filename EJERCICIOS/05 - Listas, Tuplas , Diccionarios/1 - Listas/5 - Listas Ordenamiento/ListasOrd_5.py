# Cargar una lista con 5 elementos enteros. 
# Ordenarla de menor a mayor y mostrarla por pantalla, luego ordenar de mayor a menor e imprimir nuevamente.

lista = []

for x in range(5):
    num = int(input(f"Ingresar el numero {x+1}: "))
    lista.append(num)

for k in range(4):
    for n in range(4):
        if lista[n] > lista[n+1]:
            aux = lista[n]
            lista[n] = lista[n+1]
            lista[n+1] = aux

print(f"La lista ordenada de menor a mayor es {lista}")

for k in range(4):
    for n in range(4):
        if lista[n] < lista[n+1]:
            aux = lista[n]
            lista[n] = lista[n+1]
            lista[n+1] = aux

print(f"La lista ordenada de mayor a menor es {lista}")