# 13.1 Eficiencia de memoria con tipos de datos
# Por defecto, Pandas asigna tipos amplios (int64, float64, object). Reducirlos a variantes
# más pequeñas puede ahorrar decenas de megabytes.
# Ejemplo inicial

from unicodedata import category

import pandas as pd
import numpy as np
# DataFrame grande simulado
df = pd.DataFrame({
"ID": np.arange(1, 1_000_001),
"Edad": np.random.randint(18, 90, size=1_000_000),
"Salario": np.random.randint(30_000, 120_000, size=1_000_000),
"Ciudad": np.random.choice(["Córdoba", "Buenos Aires", "Rosario"],
size=1_000_000)
})
print(df.info(memory_usage="deep"))
# 👉 Un object guarda cadenas como punteros independientes; reemplazarlo por categorías o cadenas más cortas reduce el consumo.
# Optimizar tipos numéricos
df["ID"] = df["ID"].astype("int32")
df["Edad"] = df["Edad"].astype("int8")
df["Salario"] = df["Salario"].astype("int32")
print(df.info(memory_usage="deep"))

# Optimizar texto con category
import matplotlib.pyplot as plt

df["Ciudad"] = df["Ciudad"].astype("category")
print(df.info(memory_usage="deep"))
# 💡 Combinando tipos más ajustados y categorías podés recortar más del 50 % de memoria.


# 13.2 Vectorización y evitar bucles
# Los bucles for en Python son costosos. Pandas y NumPy ofrecen operaciones vectorizadas que
# operan sobre columnas completas en C.
# Ejemplo con bucle (lento)
# Calcular impuesto (20 %) con for
df["Impuesto_for"] = [salario * 0.20 for salario in df["Salario"]]

# Versión vectorizada (rápida)
# Object 1
df["Impuesto_vec"] = df["Salario"] * 0.20

# Evitar apply cuando no es necesario
df["Salario_doble_apply"] = df["Salario"].apply(lambda x: x * 2)
df["Salario_doble_vec"] = df["Salario"] * 2
# Regla general: usá operaciones vectorizadas ⚡️ siempre que puedas y dejá apply/map para
# lógicas personalizadas difíciles de expresar con operadores nativos.


# 13.3 Trabajar con datasets grandes
# Cuando los datos exceden la memoria disponible, combiná lectura incremental, formatos eficientes
# y filtros previos.
# Leer por partes con chunksize
for chunk in pd.read_csv("datos_grandes.csv", chunksize=100_000):
    print(chunk["Salario"].mean())

# Definir tipos al cargar
df = pd.read_csv("datos.csv", dtype={"Edad": "int8", "Ciudad": "category"})

# Formatear en Parquet o Feather (formatos columnar optimizados para lectura/escritura rápida)
df.to_parquet("datos.parquet", index=False)
df = pd.read_parquet("datos.parquet")

# Filtrar antes de cargar
df = pd.read_csv("datos.csv", usecols=["ID", "Edad", "Salario"])
# 👉 Si los datos están en una base SQL, dejá que el motor filtre y agregue antes de traerlos a Pandas.