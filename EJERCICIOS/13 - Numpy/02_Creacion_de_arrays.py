import numpy as np

# Desde una lista
lista = [1, 2, 3, 4, 5]
arr1 = np.array(lista)
print("Array desde lista:", arr1)

# Desde una tupla
tupla = (10, 20, 30, 40)
arr2 = np.array(tupla)
print("Array desde tupla:", arr2)

# Array 2D (matriz)
lista2d = [[1, 2, 3], [4, 5, 6]]
arr3 = np.array(lista2d)
print("Array 2D:\n", arr3)

# Salida:
# Array desde lista: [1 2 3 4 5]
# Array desde tupla: [10 20 30 40]
# Array 2D:
# [[1 2 3]
# [4 5 6]]
# Notá que NumPy infirió automáticamente que todos los elementos son enteros.👉


# 2.2 Funciones para generar arrays
# Además de convertir listas, NumPy ofrece funciones para crear arrays de manera rápida.

# a) np.arange(start, stop, step)
# Genera un array con valores en un rango definido, similar a range() de Python, pero devuelve un array.
arr = np.arange(0, 10, 2)
print("np.arange:", arr)
# Salida:
# np.arange: [0 2 4 6 8]

# b) np.linspace(start, stop, num)
# Genera un array con una cantidad fija de elementos, distribuidos de forma equidistante entre un valor inicial y uno final.
arr = np.linspace(0, 1, 5)
print("np.linspace:", arr)
# Salida:
# np.linspace: [0. 0.25 0.5 0.75 1. ]

# Ideal cuando querés dividir un intervalo en n puntos iguales (muy usado en gráficas y 👉simulaciones).
# c) np.zeros(shape)
# Crea un array lleno de ceros.
arr = np.zeros((2, 3)) # 2 filas, 3 columnas
print("np.zeros:\n", arr)
# Salida:
# np.zeros:
# [[0. 0. 0.]
# [0. 0. 0.]]

# d) np.ones(shape)
# Crea un array lleno de unos.
arr = np.ones((3, 3))
print("np.ones:\n", arr)
# Salida:
# np.ones:
# [[1. 1. 1.]
# [1. 1. 1.]
# [1. 1. 1.]]

# e) np.eye(n)
# Genera una matriz identidad de tamaño n × n, con unos en la diagonal principal y ceros en el resto.
arr = np.eye(4)
print("np.eye:\n", arr)
# Salida:
# np.eye:
# [[1. 0. 0. 0.]
# [0. 1. 0. 0.]
# [0. 0. 1. 0.]
# [0. 0. 0. 1.]]
# Muy usada en álgebra lineal.