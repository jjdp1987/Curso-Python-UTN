#a)Indica cuántas dimensiones tiene el array:
# 1D: vector.
#2D: matriz.
#3D o más: tensores.
import numpy as np
a = np.array([1, 2, 3]) # 1D
b = np.array([[1, 2, 3], [4, 5, 6]]) # 2D
c = np.array([[[1], [2]], [[3], [4]]]) # 3D
print("a.ndim:", a.ndim) # 1
print("b.ndim:", b.ndim) # 2
print("c.ndim:", c.ndim) # 3

#b) Forma (shape)
#Devuelve una tupla con la cantidad de elementos por dimensión.
print("Forma de b:", b.shape) # (2, 3) -> 2 filas y 3 columnas

#c) Tamaño (size)
#Indica la cantidad total de elementos del array.
print("Tamaño de b:", b.size) # 6 elementos en total

#d) Tipo de datos (dtype)
#Los arrays son homogéneos: todos los elementos comparten el mismo tipo.
arr = np.array([1, 2, 3])
print("Tipo de datos:", arr.dtype) # int64 (depende del sistema)

#Si mezclás tipos, NumPy intenta unificarlos automáticamente:👉
arr = np.array([1, 2, 3.5])
print("Tipo de datos:", arr.dtype) # float64


# 3.2 Conversión de tipos (astype)
# Podemos forzar el tipo de un array usando .astype().
arr = np.array([1, 2, 3, 4])
print("Original:", arr, arr.dtype)

# Convertir a float
arr_float = arr.astype(float)
print("Convertido a float:", arr_float, arr_float.dtype)

# Convertir a string
arr_str = arr.astype(str)
print("Convertido a string:", arr_str, arr_str.dtype)
# Salida:
# Original: [1 2 3 4] int64
# Convertido a float: [1. 2. 3. 4.] float64
# Convertido a string: ['1' '2' '3' '4'] <U21


# 3.3 Indexación y slicing
# NumPy permite acceder a porciones de un array de forma similar a las listas de Python, pero con mayor poder expresivo.
# a) Indexación en 1D
arr = np.array([10, 20, 30, 40, 50])
print(arr[0]) # Primer elemento -> 10
print(arr[-1]) # Último elemento -> 50

# b) Slicing en 1D
print(arr[1:4]) # Elementos de índice 1 a 3 -> [20 30 40]
print(arr[:3]) # Primeros 3 -> [10 20 30]
print(arr[::2]) # Cada 2 elementos -> [10 30 50]

# c) Indexación en 2D
# En arrays de dos dimensiones se usa la notación [fila, columna].
mat = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print(mat[0, 0]) # Esquina superior izquierda -> 1
print(mat[1, 2]) # Fila 1, columna 2 -> 6
print(mat[-1, -1]) # Último elemento -> 9

# d) Slicing en 2D
print(mat[:2, :2]) # Submatriz 2x2 de la esquina superior izquierda
# [[1 2]
# [4 5]]
print(mat[:, 1]) # Segunda columna -> [2 5 8]
print(mat[1, :]) # Segunda fila -> [4 5 6]

# e) Indexación y slicing en ND
# En arrays con más dimensiones se agregan más índices separados por comas.
arr3d = np.array([[[1, 2], [3, 4]],
                  [[5, 6], [7, 8]]])
print(arr3d[0, 1, 1]) # Primer bloque, segunda fila, segunda columna -> 4
print(arr3d[1, :, :]) # Segundo bloque completo -> [[5 6]
# [7 8]]