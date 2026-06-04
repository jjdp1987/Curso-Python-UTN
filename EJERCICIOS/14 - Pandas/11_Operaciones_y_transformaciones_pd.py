# 7.1 Operaciones aritméticas y con funciones
# Pandas permite ejecutar operaciones directamente sobre columnas de forma vectorizada, similar a
# lo que sucede en NumPy.
# Operaciones básicas sobre columnas

import pandas as pd


datos = {
"Nombre": ["Ana", "Luis", "Carla", "Pedro"],
"Edad": [23, 35, 29, 42],
"Salario": [55000, 72000, 61000, 83000]
}
df = pd.DataFrame(datos)
# Aumentar salario en 10%
df["Salario_ajustado"] = df["Salario"] * 1.10
# Calcular el doble de la edad
df["Edad_doble"] = df["Edad"] * 2
print(df)

# Salida:
# Nombre Edad Salario Salario_ajustado Edad_doble
# 0 Ana 23 55000 60500.0 46
# 1 Luis 35 72000 79200.0 70
# 2 Carla 29 61000 67100.0 58
# 3 Pedro 42 83000 91300.0 84
# Uso de funciones matemáticas

import numpy as np
# Logaritmo del salario
df["Log_Salario"] = np.log(df["Salario"])
# Raíz cuadrada de la edad
df["Raíz_Edad"] = np.sqrt(df["Edad"])
print(df.head())

# Estas operaciones son vectorizadas: se aplican a toda la 👉 columna de forma eficiente, mucho más
# rápido que iterar con for.
# 7.2 Aplicación de funciones personalizadas (apply, map)
# En ocasiones necesitamos lógicas propias para transformar los datos. Las funciones map(),
# apply() y el método DataFrame.map() permiten incorporar reglas personalizadas.


# map(): aplicar funciones sobre una Serie
# Convertir nombres a mayúsculas
df["Nombre_mayus"] = df["Nombre"].map(str.upper)
# Evaluar si la edad es par o impar
df["Edad_paridad"] = df["Edad"].map(lambda x: "Par" if x % 2 == 0 else "Impar")
print(df)
# apply(): operar sobre columnas o filas
# Calcular impuestos (20% del salario)
df["Impuesto"] = df["Salario"].apply(lambda x: x * 0.20)
# Calcular ingreso neto fila por fila
df["Ingreso_neto"] = df.apply(lambda fila: fila["Salario"] - fila["Impuesto"],
axis=1)
# 👉 Recordá que axis=0 opera sobre columnas y axis=1 sobre filas.
# DataFrame.map(): transformar todo el DataFrame
# Crear un mini DataFrame de números
df_num = pd.DataFrame([[1, -2], [3, -4]], columns=["A", "B"])
# Aplicar valor absoluto a cada elemento
df_abs = df_num.map(abs)
print(df_abs)
# 7.3 Renombrar columnas y filas
# Renombrar columnas o índices ayuda a documentar mejor los datos y preparar reportes más claros.
# Renombrar columnas
# Renombrar columnas específicas
df_renombrado = df.rename(columns={"Nombre": "Empleado", "Edad": "Años"})
print(df_renombrado.head())
# Renombrar todas las columnas de una vez
df.columns = [
"Empleado", "Años", "Sueldo", "Salario_ajustado",
"Edad_doble", "Log_Salario", "Raíz_Edad",
"Nombre_mayus", "Edad_paridad", "Impuesto", "Ingreso_neto"
]
print(df.head())
# Renombrar índices (filas)
# Asignar índices personalizados con set_axis
df = df.set_axis(["Fila1", "Fila2", "Fila3", "Fila4"], axis="index")
print(df.head())
# Renombrar índices específicos
df = df.rename(index={"Fila1": "Registro_Ana", "Fila2": "Registro_Luis"})
print(df.head())