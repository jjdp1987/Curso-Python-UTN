# Ejercicio 1: Crear un array con los números del 1 al 10 y calcular el array al cuadrado, la suma total y la media.
import numpy as np

arr = np.arange(1, 11)
print("Array:", arr)
# Array al cuadrado
print("Cuadrados:", arr ** 2)
# Suma total
print("Suma:", arr.sum())
# Media
print("Media:", arr.mean())
# Salida:
# Array: [ 1 2 3 4 5 6 7 8 9 10]
# Cuadrados: [ 1 4 9 16 25 36 49 64 81 100]
# Suma: 55
# Media: 5.5