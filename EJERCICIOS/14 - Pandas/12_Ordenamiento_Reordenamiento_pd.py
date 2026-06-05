# 8.1 Ordenar por índice (sort_index)
# El índice identifica cada fila o columna. Si lo personalizás también podés ordenarlo para presentar
# la información con otro criterio.
# Ejemplo de DataFrame

import pandas as pd
datos = {
"Nombre": ["Ana", "Luis", "Carla", "Pedro", "María"],
"Edad": [23, 35, 29, 42, 31],
"Salario": [55000, 72000, 61000, 83000, 59000]
}
df = pd.DataFrame(datos)
df = df.set_axis(["e", "a", "c", "d", "b"], axis="index") # indices
# personalizados
print(df)

# Salida:
# Nombre Edad Salario
# e Ana 23 55000
# a Luis 35 72000
# c Carla 29 61000
# d Pedro 42 83000
# b María 31 59000


# Ordenar filas por índice
df_ordenado = df.sort_index()
print(df_ordenado)

# Salida:
# Nombre Edad Salario
# a Luis 35 72000
# b María 31 59000
# c Carla 29 61000
# d Pedro 42 83000
# e Ana 23 55000

# 👉 De manera predeterminada, sort_index() ordena de forma ascendente.

# Ordenar filas en orden descendente
df_desc = df.sort_index(ascending=False)
print(df_desc)

# Ordenar columnas por índice
df_col = df.sort_index(axis=1) # ordena las columnas alfabéticamente
print(df_col)

# 👉 Recordá que axis=0 referencia filas (por defecto) y axis=1 columnas.



# 8.2 Ordenar por valores (sort_values)
# Cuando importan los valores de una columna, sort_values() permite reorganizar datos según
# uno o varios criterios.
# Ordenar por una columna
# Ordenar por Edad
df_edad = df.sort_values(by="Edad")
print(df_edad)

# Salida:
# Nombre Edad Salario
# e Ana 23 55000
# c Carla 29 61000
# b María 31 59000
# a Luis 35 72000
# d Pedro 42 83000
# Ordenar en orden descendente

# Ordenar por Salario descendente
df_salario = df.sort_values(by="Salario", ascending=False)
print(df_salario)

# Ordenar por varias columnas
# Primero por Edad y, en caso de empate, por Salario
df_multi = df.sort_values(by=["Edad", "Salario"])
print(df_multi)

# Ordenar manteniendo orden estable
# Mantener el orden estable cuando hay empates
df_estable = df.sort_values(by="Edad", kind="mergesort")
print(df_estable)