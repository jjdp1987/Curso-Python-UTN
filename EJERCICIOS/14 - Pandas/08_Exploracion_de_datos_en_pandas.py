# 4.1 Inspección rápida con .head(), .tail(), .info(),
# .describe()
# Pandas ofrece funciones muy útiles para observar rápidamente nuestros datos:
# • head(): muestra las primeras filas.
# • tail(): muestra las últimas filas.
# • info(): informa tipos de datos y valores no nulos.
# • describe(): genera estadísticas descriptivas.
# Ejemplo práctico

import pandas as pd


# Ejemplo de DataFrame
datos = {
"Nombre": ["Ana", "Luis", "Carla", "Pedro", "María"],
"Edad": [23, 35, 29, 42, 31],
"Ciudad": ["Córdoba", "Buenos Aires", "Rosario", "Mendoza", "Salta"],
"Salario": [55000, 72000, 61000, 83000, 59000]
}
df = pd.DataFrame(datos)
print(df.head(3)) # primeras 3 filas
print(df.tail(2)) # últimas 2 filas
print(df.info())
print(df.describe())

# Salida resumida:
# Nombre Edad Ciudad Salario
# 0 Ana 23 Córdoba 55000
# 1 Luis 35 Buenos Aires 72000
# 2 Carla 29 Rosario 61000
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 5 entries, 0 to 4
# Data columns (total 4 columns):
# # Column Non-Null Count Dtype
# --- ------ -------------- -----
# 0 Nombre 5 non-null object
# 1 Edad 5 non-null int64
# 2 Ciudad 5 non-null object
# 3 Salario 5 non-null int64
# dtypes: int64(2), object(2)
# memory usage: 288.0 bytes
# Edad Salario
# count 5.000000 5.000000
# mean 32.000000 66000.000000
# std 7.141428 11180.339887
# min 23.000000 55000.000000
# 25% 29.000000 59000.000000
# 50% 31.000000 61000.000000
# 75% 35.000000 72000.000000
# max 42.000000 83000.000000

# Con estas salidas sabemos cuántas filas y columnas existen, l 👉 os tipos de datos, los valores no
# nulos y un resumen estadístico. También podés incluir columnas de texto en describe() con
# df.describe(include="object").


# 4.2 Tipos de datos y conversión con astype()
# Cada columna de un DataFrame tiene un tipo de dato:
# int64: enteros.
# float64: números decimales.
# object: texto.
# datetime64: fechas.

# Ver tipos de datos
print(df.dtypes)

# Salida:
# Nombre object
# Edad int64
# Ciudad object
# Salario int64
# dtype: object

# Convertir tipos con astype
# Convertir Edad a float
df["Edad"] = df["Edad"].astype(float)
# Convertir Salario a string
df["Salario"] = df["Salario"].astype(str)
print(df.dtypes)

# 👉 Resulta muy útil para preparar datos antes de un modelo de Machine Learning o cuando una
# columna se cargó con el tipo incorrecto.
# Conversión a fechas
# Ejemplo de columna con fechas en texto
df_fechas = pd.DataFrame({"Fecha": ["2025-01-01", "2025-02-15", "2025-03-20"]})
# Convertir a tipo datetime
df_fechas["Fecha"] = pd.to_datetime(df_fechas["Fecha"])
print(df_fechas.dtypes)

# Salida:
# Fecha datetime64[ns]
# dtype: object
# 4.3 Manejo de índices y etiquetas
# El índice identifica cada fila. Por defecto es un entero secuencial, pero se puede personalizar para
# mejorar la lectura.
# Ver índices actuales
print(df.index)
# Salida:
# RangeIndex(start=0, stop=5, step=1)
# Asignar un índice personalizado
df_personalizado = df.set_index("Nombre")
print(df_personalizado)
# Salida:
# Edad Ciudad Salario
# Nombre
# Ana 23 Córdoba 55000
# Luis 35 Buenos Aires 72000
# Carla 29 Rosario 61000
# Pedro 42 Mendoza 83000
# María 31 Salta 59000

# 👉 Ahora la columna Nombre actúa como identificador de cada fila.
# Resetear índices y renombrar columnas
df_reset = df_personalizado.reset_index()
print(df_reset.head())
df.rename(columns={"Nombre": "Empleado", "Ciudad": "Localidad"}, inplace=True)
print(df.head())
# 👉 Manejar bien los índices y etiquetas facilita un análisis claro y reproducible.