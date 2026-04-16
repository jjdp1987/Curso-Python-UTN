# Medir el tiempo de ejecución de dos funciones que ordenan una lista, primero sin uso de
# decoradores y luego empleando decoradores.
# Programa:

import random
import time

# Ordenamiento Burbuja

def burbuja(lista):
    inicio = time.time()
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    fin = time.time()
    print(f"Tiempo Burbuja: {fin - inicio:.4f} segundos")

# Ordenamiento Quicksort

def quicksort(lista):
    inicio = time.time()
    def _quicksort(arr):
        if len(arr) <= 1:
            return arr
        pivote = arr[len(arr) // 2]
        izquierda = [x for x in arr if x < pivote]
        medio = [x for x in arr if x == pivote]
        derecha = [x for x in arr if x > pivote]
        return _quicksort(izquierda) + medio + _quicksort(derecha)
        resultado = _quicksort(lista)
        fin = time.time()
        print(f"Tiempo Quicksort: {fin - inicio:.4f} segundos")
        return resultado


# Generar listas con 10000 elementos aleatorios
lista1 = [random.randint(0, 100000) for _ in range(10000)]
lista2 = lista1[:] # copia para quicksort
# Ejecutar
burbuja(lista1[:]) # paso copia para no modificar la lista original
quicksort(lista2)