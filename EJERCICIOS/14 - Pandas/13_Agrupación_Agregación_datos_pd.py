# 9.1 Uso de groupby
# groupby separa un DataFrame en grupos según columnas elegidas y prepara los datos para
# agregaciones.
# Ejemplo de DataFrame
import pandas as pd
datos = {
"Empleado": ["Ana", "Luis", "Carla", "Pedro", "María", "Jorge"],
"Departamento": ["Ventas", "Ventas", "IT", "IT", "Ventas", "IT"],
"Salario": [55000, 72000, 61000, 83000, 59000, 75000],
"Edad": [23, 35, 29, 42, 31, 38]
}
df = pd.DataFrame(datos)
print(df)

# Salida:
# Empleado Departamento Salario Edad
# 0 Ana Ventas 55000 23
# 1 Luis Ventas 72000 35
# 2 Carla IT 61000 29
# 3 Pedro IT 83000 42
# 4 María Ventas 59000 31
# 5 Jorge IT 75000 38

# Agrupar por una columna
grupo = df.groupby("Departamento")
print(grupo)
# 👉 El resultado es un objeto DataFrameGroupBy; la agregación llega cuando aplicás funciones
# como mean() o agg().

# 9.2 Funciones de agregación (sum, mean, count)
# Una vez agrupados, aplicás funciones de agregación para obtener indicadores por grupo.
# Calcular la media por grupo
print(df.groupby("Departamento")["Salario"].mean())

# Salida:
# Departamento
# IT 73000.0
# Ventas 62000.0
# Name: Salario, dtype: float64

# Calcular varias métricas
print(df.groupby("Departamento")["Edad"].sum())
print(df.groupby("Departamento")["Edad"].count())

# Agregación sobre columnas numéricas
df_promedios = df.groupby("Departamento")[["Salario", "Edad"]].mean()
print(df_promedios)

# Salida:
# Salario Edad

# Departamento
# IT 73000.0 36.333333
# Ventas 62000.0 29.666667
# Seleccioná las columnas 👉 numéricas con doble corchete (o usá numeric_only=True) para
# evitar errores en versiones recientes de Pandas.
# 9.3 Agregaciones múltiples y personalizadas
# Con agg() podés combinar funciones estándar y lógicas propias en una sola llamada.
# Agregaciones múltiples
print(df.groupby("Departamento")["Salario"].agg(["sum", "mean", "max"]))
# Salida:
# sum mean max

# Departamento
# IT 219000 73000.0 83000
# Ventas 186000 62000.0 72000
# Agregación sobre varias columnas
print(df.groupby("Departamento").agg({
"Salario": ["mean", "max"],
"Edad": ["min", "max"]
}))

# Salida:
# Salario Edad
# mean max min max
# Departamento
# IT 73000.0 83000 29 42
# Ventas 62000.0 72000 23 35

# Funciones personalizadas con agg()
def rango(x):
    return x.max() - x.min()
print(df.groupby("Departamento").agg({
"Salario": rango,
"Edad": rango
}))

# Salida:
# Salario Edad
# Departamento
# IT 22000 13
# Ventas 17000 12
# Con funciones personalizadas obtenés indicadores 👉 propios, como el rango de salarios o edades
# por equipo.