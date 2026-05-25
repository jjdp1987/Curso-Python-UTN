# 5.1 reshape : cambiar la forma de un array
# Con reshape podemos cambiar la forma de un array, siempre que la cantidad de elementos
# se mantenga.

import numpy as np
arr = np.arange(12) # Array de 0 a 11
print("Array original:\n", arr)
mat = arr.reshape(3, 4) # 3 filas, 4 columnas
print("Array con reshape (3x4):\n", mat)
# Salida:
# Array original:
# [ 0 1 2 3 4 5 6 7 8 9 10 11]
# Array con reshape (3x4):
# [[ 0 1 2 3]
# [ 4 5 6 7]
# [ 8 9 10 11]]
# 👉 Podemos usar -1 para que NumPy calcule automáticamente una dimensión:
# mat = arr.reshape(-1, 6) # NumPy ajusta la cantidad de filas
# print(mat)


# 5.2 Concatenación y apilamiento
# NumPy permite unir arrays de distintas maneras.

# a) Concatenación ( np.concatenate )
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.concatenate([a, b])
print("Concatenación:", c) # [1 2 3 4 5 6]

# b) Apilamiento horizontal ( np.hstack )
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print("Apilamiento horizontal:\n", np.hstack([a, b]))
# Salida:
# Apilamiento horizontal:
# [[1 2 5 6]
# [3 4 7 8]]

# c) Apilamiento vertical ( np.vstack )
print("Apilamiento vertical:\n", np.vstack([a, b]))
# Salida:
# Apilamiento vertical:
# [[1 2]
# [3 4]
# [5 6]
# [7 8]]
# 👉 Muy útil para unir datasets o matrices.


# 5.3 División de arrays ( split )
# Podemos dividir un array en sub-arrays con np.split y funciones relacionadas.

# a) División en 1D
arr = np.arange(10) # [0 1 2 3 4 5 6 7 8 9]
dividido = np.split(arr, 2) # Divide en 2 partes iguales
print("División en 2 partes:", dividido)
# Salida:
# División en 2 partes: [array([0, 1, 2, 3, 4]), array([5, 6, 7, 8, 9])]

# b) División en 2D
mat = np.arange(16).reshape(4, 4)
print("Matriz original:\n", mat)
# Dividir en 2 bloques horizontales
print("División vertical:\n", np.vsplit(mat, 2))
# Dividir en 2 bloques verticales
print("División horizontal:\n", np.hsplit(mat, 2))


# 5.4 Transposición y permutación de ejes

# a) Transposición ( .T )
# Cambia filas por columnas, similar a la transpuesta en álgebra lineal.
mat = np.array([[1, 2, 3],
                [4, 5, 6]])
print("Matriz original:\n", mat)
print("Transpuesta:\n", mat.T)
# Salida:
# Matriz original:
# [[1 2 3]
# [4 5 6]]
# Transpuesta:
# [[1 4]
# [2 5]
# [3 6]]

# b) Permutación de ejes ( np.transpose o np.swapaxes )
# Para arrays con más dimensiones, podemos reordenar los ejes.
arr3d = np.arange(24).reshape(2, 3, 4) # 2 bloques, 3 filas, 4 columnas
print("Forma original:", arr3d.shape) # (2, 3, 4)
arr_perm = np.transpose(arr3d, (1, 0, 2))
print("Forma permutada:", arr_perm.shape) # (3, 2, 4)
# 👉 Esto es clave cuando trabajamos con imágenes (alto, ancho, canales) o series temporales.