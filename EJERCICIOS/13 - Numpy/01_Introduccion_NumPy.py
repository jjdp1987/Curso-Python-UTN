# Para instalar NumPy, se usa pip (el gestor de paquetes de Python):
# pip install numpy
# Una vez instalado, la convención es importarlo con el alias np :
import numpy as np
# Crear un array simple
arr = np.array([10, 20, 30, 40])
print("Array de NumPy:", arr)
print("Tipo:", type(arr))

# Lista de Python
lista = [1, 2, 3, 4, 5]
# Intentar sumar 2 a cada elemento
nueva_lista = [x + 2 for x in lista]
print(nueva_lista) # [3, 4, 5, 6, 7]

# Crear un array de NumPy
arr = np.array([1, 2, 3, 4, 5])
# Operaciones vectorizadas
print(arr + 2) # [3 4 5 6 7]
print(arr * 3) # [ 3 6 9 12 15]
print(arr ** 2) # [ 1 4 9 16 25]


# Ventajas de NumPy sobre listas
# Mucho más rápido (usa código optimizado en C).
# Ocupa menos memoria.
# Permite trabajar con matrices y tensores de varias dimensiones.
# Incluye funciones matemáticas listas para usar.