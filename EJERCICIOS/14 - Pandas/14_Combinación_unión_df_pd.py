# 10.1 Concatenación (concat)
# concat permite unir DataFrames por filas o columnas, manteniendo el orden de los datos originales.
# Concatenar por filas
import pandas as pd
df1 = pd.DataFrame({
"ID": [1, 2, 3],
"Nombre": ["Ana", "Luis", "Carla"]
})
df2 = pd.DataFrame({
"ID": [4, 5],
"Nombre": ["Pedro", "María"]
})
df_concat = pd.concat([df1, df2])
print(df_concat)

# Salida:
# ID Nombre
# 0 1 Ana
# 1 2 Luis
# 2 3 Carla
# 0 4 Pedro
# 1 5 María

# Los índices se conservan. Para regenerarlos usá 👉ignore_index=True.
# Resetear índices tras concatenar
df_concat = pd.concat([df1, df2], ignore_index=True)
# Concatenar por columnas
df3 = pd.DataFrame({
"Edad": [23, 35, 29]
})
df_col = pd.concat([df1, df3], axis=1)
print(df_col)

# Salida:
# ID Nombre Edad
# 0 1 Ana 23
# 1 2 Luis 35
# 2 3 Carla 29



# 10.2 Uniones estilo SQL (merge, join)
# merge replica las uniones de SQL sobre columnas clave, mientras que join trabaja con índices.
# Inner join con merge

empleados = pd.DataFrame({
"ID": [1, 2, 3],
"Nombre": ["Ana", "Luis", "Carla"]
})
salarios = pd.DataFrame({
"ID": [1, 2, 4],
"Salario": [55000, 72000, 83000]
})
df_merge = pd.merge(empleados, salarios, on="ID")
print(df_merge)

# Salida:
# ID Nombre Salario
# 0 1 Ana 55000
# 1 2 Luis 72000

# El inner join devuelve solo registros con claves presentes en ambos DataFrames.👉
# Otros tipos de uniones
df_left = pd.merge(empleados, salarios, on="ID", how="left")
df_right = pd.merge(empleados, salarios, on="ID", how="right")
df_outer = pd.merge(empleados, salarios, on="ID", how="outer")

# Unir por índice con join
df1 = pd.DataFrame({"Edad": [23, 35, 29]}, index=["Ana", "Luis", "Carla"])
df2 = pd.DataFrame({"Salario": [55000, 72000, 61000]}, index=["Ana", "Luis", "Carla"])
df_join = df1.join(df2)
print(df_join)

# Salida:
# Edad Salario
# Ana 23 55000
# Luis 35 72000
# Carla 29 61000



# 10.3 Apilado y des-apilado (stack, unstack)
# Estas funciones reorganizan la estructura de un DataFrame al alternar entre formato ancho y largo.
# Ejemplo base
df = pd.DataFrame({
"Empleado": ["Ana", "Luis"],
"Departamento": ["Ventas", "IT"],
"Salario": [55000, 72000]
})
df = df.set_index(["Empleado", "Departamento"])
print(df)

# Salida:
# Salario
# Empleado Departamento
# Ana Ventas 55000
# Luis IT 72000

# stack(): columnas a filas
df_stack = df.stack()
print(df_stack)

# Salida:
# Empleado Departamento
# Ana Ventas Salario 55000
# Luis IT Salario 72000
# dtype: int64

# unstack(): índices a columnas
df_unstack = df.unstack()
print(df_unstack)

# Salida:
# Salario
# Departamento IT Ventas
# Empleado
# Ana NaN 55000.0
# Luis 72000.0 NaN

# Alternar con 👉stack() y unstack() es clave para armar tablas dinámicas y pivotes.