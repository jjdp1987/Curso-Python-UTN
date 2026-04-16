# Medir el tiempo de ejecución de dos funciones empleando decoradores de clase.
# Programa:

import random
import time

# Decorador de clase para medir tiempo

class MedirTiempo:
    def __init__(self, func):
        self.func = func # Guardamos la función original
    def __call__(self, *args, **kwargs):
        inicio = time.time()
        resultado = self.func(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo {self.func.__name__}: {fin - inicio:.4f} segundos")
        return resultado
    
# Ordenamiento Burbuja @MedirTiempo

def burbuja(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Ordenamiento Quicksort @MedirTiempo

def quicksort(lista):
    def _quicksort(arr):
        if len(arr) <= 1:
            return arr
        pivote = arr[len(arr) // 2]
        izquierda = [x for x in arr if x < pivote]
        medio = [x for x in arr if x == pivote]
        derecha = [x for x in arr if x > pivote]
        return _quicksort(izquierda) + medio + _quicksort(derecha)
    return _quicksort(lista)

# Generar listas con 10000 elementos aleatorios

lista1 = [random.randint(0, 100000) for _ in range(10000)]
lista2 = [random.randint(0, 100000) for _ in range(10000)]

# Ejecutar

burbuja(lista1)
quicksort(lista2)