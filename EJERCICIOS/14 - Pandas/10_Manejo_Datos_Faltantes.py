# 6.1 Detección de valores nulos (isnull, notnull)
# En Pandas los valores faltantes se representan como NaN. Podemos identificarlos rápidamente
# usando los métodos isnull() y notnull().
# Crear un DataFrame con valores nulos

import pandas as pd
import numpy as np


datos = {
"Nombre": ["Ana", "Luis", "Carla", "Pedro", "María"],
"Edad": [23, np.nan, 29, 42, None],
"Ciudad": ["Córdoba", "Buenos Aires", None, "Mendoza", "Salta"],
"Salario": [55000, 72000, None, 83000, 59000]
}
df = pd.DataFrame(datos)
print(df)

# Salida:
# Nombre Edad Ciudad Salario
# 0 Ana 23.0 Córdoba 55000.0
# 1 Luis NaN Buenos Aires 72000.0
# 2 Carla 29.0 None NaN
# 3 Pedro 42.0 Mendoza 83000.0
# 4 María NaN Salta 59000.0

# isnull() detecta valores nulos
print(df.isnull())

# Salida:
# Nombre Edad Ciudad Salario
# 0 False False False False
# 1 False True False False
# 2 False False True True
# 3 False False False False
# 4 False True False False

# notnull() detecta valores NO nulos
print(df.notnull())

# Contar valores nulos por columna
print(df.isnull().sum())

# Salida:
# Nombre 0
# Edad 2
# Ciudad 1
# Salario 1
# dtype: int64
# Con esto sabés 👉 en qué columnas y cuántos datos faltan.



# 6.2 Eliminación de datos (dropna)
# A veces lo más simple es eliminar filas o columnas que contienen valores faltantes. dropna()
# ofrece varios parámetros para controlar la limpieza.
# Eliminar filas con cualquier valor nulo

df_sin_nulos = df.dropna()
print(df_sin_nulos)

# Eliminar columnas con cualquier valor nulo
df_sin_columnas = df.dropna(axis=1)
print(df_sin_columnas)

# Eliminar filas solo si todos los valores son nulos
df_sin_todos = df.dropna(how="all")

# Eliminar filas si tienen menos de un mínimo de valores no nulos
df_min = df.dropna(thresh=3) # conserva filas con al menos 3 valores válidos

# 👉 Esta estrategia puede ser útil, pero cuidado: eliminar datos reduce el tamaño del dataset.



# 6.3 Imputación y reemplazo (fillna, replace)
# Cuando no queremos eliminar información, podemos rellenar valores faltantes con distintos
# métodos o reemplazar datos problemáticos.
# Rellenar con un valor fijo
df_relleno = df.fillna(0)
print(df_relleno)

# Rellenar con la media, mediana o moda

# Rellenar Edad con la media
df["Edad"].fillna(df["Edad"].mean(), inplace=True)

# Rellenar Salario con la mediana
df["Salario"].fillna(df["Salario"].median(), inplace=True)

# Rellenar Ciudad con un valor por defecto
df["Ciudad"].fillna("Desconocida", inplace=True)

# Rellenar hacia adelante o hacia atrás

# Forward fill (usa el valor anterior)
# usar ffill() en lugar de fillna(method=...) evita warnings/errores de tipos
df_ffill = df.ffill()

# Backward fill (usa el valor siguiente)
df_bfill = df.bfill()

# Reemplazar valores específicos (replace)

# Reemplazar None por un texto fijo
df["Ciudad"].replace({None: "Sin ciudad"}, inplace=True)

# Reemplazar un salario por otro valor
df["Salario"].replace({59000: 60000}, inplace=True)

# El manejo correcto de valores faltantes es esencial: un mal tratamiento pue 👉 de sesgar resultados o
# hacer fallar modelos.