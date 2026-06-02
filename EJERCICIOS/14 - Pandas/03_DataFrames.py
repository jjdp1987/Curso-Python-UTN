# 2.2 DataFrames
# El DataFrame es la estructura estrella de Pandas: se asemeja a una tabla de Excel o SQL,
# con filas identificadas por un índice y columnas con nombres. Puede crearse a partir de
# múltiples fuentes de datos.
import numpy as np
import pandas as pd

# 1) Desde un diccionario de listas
datos = {
"Nombre": ["Ana", "Luis", "Carla", "Pedro"],
"Edad": [23, 35, 29, 42],
"Ciudad": ["Córdoba", "Buenos Aires", "Rosario", "Mendoza"]
}
df = pd.DataFrame(datos)
print(df)
# Salida esperada:
# Nombre Edad Ciudad
# 0 Ana 23 Córdoba
# 1 Luis 35 Buenos Aires
# 2 Carla 29 Rosario
# 3 Pedro 42 Mendoza


# 2) Desde una lista de diccionarios
datos2 = [
{"Nombre": "Ana", "Edad": 23, "Ciudad": "Córdoba"},
{"Nombre": "Luis", "Edad": 35, "Ciudad": "Buenos Aires"},
{"Nombre": "Carla", "Edad": 29, "Ciudad": "Rosario"}
]
df2 = pd.DataFrame(datos2)
print(df2)


# 3) Desde un array de NumPy

matriz = np.array([[10, 20, 30], [40, 50, 60]])
df3 = pd.DataFrame(matriz, columns=["A", "B", "C"])
print(df3)
# Salida esperada:
# A B C
# 0 10 20 30
# 1 40 50 60


# Operaciones básicas con DataFrames
# Ver primeras filas
print(df.head())
# Seleccionar una columna
print(df["Nombre"])
# Seleccionar varias columnas
print(df[["Nombre", "Edad"]])
# Seleccionar una fila por índice
print(df.loc[0]) # por etiqueta
print(df.iloc[2]) # por posición
# Estadísticas rápidas
print(df.describe())