import numpy as np

# 8.1 Producto punto ( dot )
# El producto punto puede calcularse entre vectores o matrices compatibles.

# Producto punto entre vectores
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
print("8.1 Producto punto (vectores):", np.dot(v1, v2)) # 32
# 1*4 + 2*5 + 3*6 = 32
# 👉 También funciona entre matrices:
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])
print("8.1 Producto punto (matrices):\n", np.dot(A, B))
# [[1*5 + 2*7, 1*6 + 2*8],
#  [3*5 + 4*7, 3*6 + 4*8]]
# Salida:
# [[19 22]
# [43 50]]


# 8.2 Multiplicación de matrices
# NumPy ofrece varias formas de multiplicar matrices:
# np.dot(A, B) : producto matricial.
# A @ B : operador legible (Python 3.5+).
# np.matmul(A, B) : equivalente, pensado para matrices.
print("8.2 Usando @:\n", A @ B)
print("8.2 Usando matmul:\n", np.matmul(A, B))
# 👉 La multiplicación elemento a elemento se realiza con * , no con dot :
print("8.2 Multiplicación elemento a elemento:\n", A * B)


# 8.3 Matrices identidad e inversas

# a) Matriz identidad
# La matriz identidad cumple el rol del “1” en álgebra lineal.
I = np.eye(3)
print("8.3 Matriz identidad 3x3:\n", I)
# Salida:
# [[1. 0. 0.]
# [0. 1. 0.]
# [0. 0. 1.]]

# b) Inversa de una matriz
# La matriz inversa A⁻¹ (si existe) satisface A @ A⁻¹ = I .
A = np.array([[1, 2],
              [3, 4]])
A_inv = np.linalg.inv(A)
print("8.3 Matriz inversa:\n", A_inv)
# Verificar
print("8.3 A @ A_inv:\n", A @ A_inv)
# Salida (aprox.):
# Matriz inversa:
# [[-2. 1. ]
# [ 1.5 -0.5]]
# A @ A_inv:
# [[1. 0.]
# [0. 1.]]


# 8.4 Determinantes y autovalores

# a) Determinante ( np.linalg.det )
# Permite saber si una matriz es invertible y aparece en múltiples cálculos.
A = np.array([[1, 2],
              [3, 4]])
det = np.linalg.det(A)
print("8.4 Determinante:", det) # -2.0...

# b) Autovalores y autovectores ( np.linalg.eig )
# Se utilizan en reducción de dimensionalidad (PCA) y modelos matemáticos.
A = np.array([[2, 0],
              [0, 3]])
valores, vectores = np.linalg.eig(A)
print("8.4 Autovalores:", valores)
print("8.4 Autovectores:\n", vectores)
# Salida:
# Autovalores: [2. 3.]
# Autovectores:
# [[1. 0.]
# [0. 1.]]
# 👉 Como la matriz es diagonal, los autovalores coinciden con sus elementos
# principales.