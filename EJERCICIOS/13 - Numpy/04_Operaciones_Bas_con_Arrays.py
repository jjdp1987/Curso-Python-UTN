# Podemos aplicar directamente operaciones aritméticas ( + , - , * , / , ** ) sobre arrays;
# NumPy las ejecuta elemento por elemento.

# 4.1 Operaciones aritméticas elemento a elemento

import numpy as np
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])
print("Suma:", a + b) # [11 22 33 44]
print("Resta:", b - a) # [ 9 18 27 36]
print("Multiplicación:", a * b) # [ 10 40 90 160]
print("División:", b / a) # [10. 10. 10. 10.]
print("Potencia:", a ** 2) # [ 1 4 9 16]

# 4.2 Broadcasting en NumPy
# El broadcasting permite operar entre arrays de diferentes tamaños o formas, siempre que se
# cumplan reglas específicas.

# Ejemplo 1: sumar un escalar a un array.
arr = np.array([1, 2, 3, 4])
print(arr + 5) # [6 7 8 9]

# Ejemplo 2: operaciones entre un array 2D y uno 1D.
mat = np.array([[1, 2, 3],
                [4, 5, 6]])
vec = np.array([10, 20, 30])
print(mat + vec)
# Salida:
# [[11 22 33]
# [14 25 36]]

# 👉 NumPy expande el array más pequeño para que coincida en dimensiones con el mayor.

# 4.3 Funciones matemáticas comunes
# NumPy incluye funciones que operan elemento a elemento (ufuncs, universal functions).

# a) Raíz cuadrada ( np.sqrt )
arr = np.array([1, 4, 9, 16])
print("Raíz cuadrada:", np.sqrt(arr)) # [1. 2. 3. 4.]

# b) Exponencial ( np.exp )
arr = np.array([0, 1, 2])
print("Exponencial:", np.exp(arr)) # [1. 2.71828183 7.3890561 ]

# c) Logaritmo natural ( np.log )
arr = np.array([1, np.e, np.e**2])
print("Logaritmo natural:", np.log(arr)) # [0. 1. 2.]

# d) Funciones trigonométricas ( np.sin , np.cos )
arr = np.array([0, np.pi/2, np.pi])
print("Seno:", np.sin(arr)) # [0. 1. 0.]
print("Coseno:", np.cos(arr)) # [ 1. 0. -1.]