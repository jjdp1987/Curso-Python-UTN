import numpy as np

# 6.1 Indexación booleana
# Consiste en aplicar una condición lógica sobre un array. El resultado es otro array con
# valores True / False que usamos para filtrar.

arr = np.array([10, 20, 30, 40, 50])
# Crear un filtro booleano
filtro = arr > 25
print("6.1 Filtro booleano:", filtro)
# Aplicar filtro al array
print("6.1 Elementos mayores a 25:", arr[filtro])
# Salida:
# Filtro booleano: [False False True True True]
# Elementos mayores a 25: [30 40 50]
# 👉 Muy útil para aplicar condiciones sin escribir bucles.


# 6.2 Uso de máscaras
# Una máscara es un array booleano que enmascara valores de interés.
# a) Máscara simple

arr = np.arange(1, 11) # [1 2 3 4 5 6 7 8 9 10]
mascara = arr % 2 == 0 # Números pares
print("6.2 Máscara:", mascara)
print("6.2 Números pares:", arr[mascara])
# Salida:
# Máscara: [False True False True False True False True False True]
# Números pares: [ 2 4 6 8 10]

# b) Máscara combinada
# Podemos combinar condiciones con operadores lógicos: & (AND), | (OR) y ~ (NOT).
# Seleccionar números mayores a 3 y menores a 8
mascara = (arr > 3) & (arr < 8)
print("6.2 Condición (3 < arr < 8):", arr[mascara])
# Salida:
# Condición (3 < arr < 8): [4 5 6 7]


# 6.3 Filtrado condicional con np.where
# La función np.where devuelve los índices donde se cumple una condición. También sirve
# como un if vectorizado.

# a) Obtener índices
arr = np.array([5, 10, 15, 20, 25])
indices = np.where(arr > 12)
print("6.3 Índices de elementos > 12:", indices)
print("6.3 Elementos:", arr[indices])
# Salida:
# Índices de elementos > 12: (array([2, 3, 4]),)
# Elementos: [15 20 25]

# b) If vectorizado
# Podemos usar np.where(condición, valor_si_verdadero, valor_si_falso) .
arr = np.array([5, 10, 15, 20, 25])
# Si el elemento es mayor a 15 "Alto", si no "Bajo"
resultado = np.where(arr > 15, "Alto", "Bajo")
print("6.3 Clasificación:", resultado)
# Salida:
# Clasificación: ['Bajo' 'Bajo' 'Bajo' 'Alto' 'Alto']