# 5.1 Selección por etiquetas (.loc)
# Con loc accedemos a filas y columnas usando nombres de etiquetas (no números).

import pandas as pd
datos = {
"Nombre": ["Ana", "Luis", "Carla", "Pedro", "María"],
"Edad": [23, 35, 29, 42, 31],
"Ciudad": ["Córdoba", "Buenos Aires", "Rosario", "Mendoza", "Salta"],
"Salario": [55000, 72000, 61000, 83000, 59000]
}
df = pd.DataFrame(datos)
df = df.set_index("Nombre") # usamos Nombre como índice
print(df)

# Salida:
# Edad Ciudad Salario
# Nombre
# Ana 23 Córdoba 55000
# Luis 35 Buenos Aires 72000
# Carla 29 Rosario 61000
# Pedro 42 Mendoza 83000
# María 31 Salta 59000

# Ejemplos con loc Seleccionar una fila por etiqueta
print(df.loc["Carla"])

# Seleccionar varias filas
print(df.loc[["Ana", "Pedro"]])

# Seleccionar filas y columnas específicas
print(df.loc["Luis", "Ciudad"]) # valor único
print(df.loc[["Ana", "María"], ["Edad", "Salario"]])



# 5.2 Selección por posición (.iloc)
# Con iloc seleccionamos datos según su posición numérica, al estilo de un array de NumPy. Seleccionar la primera fila
print(df.iloc[0])

# Seleccionar la tercera fila y segunda columna
print(df.iloc[2, 1])

# Seleccionar un rango de filas
print(df.iloc[1:4]) # filas 1 a 3

# Seleccionar rango de filas y columnas
print(df.iloc[0:2, 0:2]) # primeras 2 filas y 2 columnas

# 👉 loc es más legible cuando conocemos los nombres, mientras que iloc es práctico para
# operaciones numéricas o iteraciones controladas.



# 5.3 Filtrado con condiciones lógicas
# Podemos aplicar expresiones lógicas para filtrar filas según criterios específicos.
# Filtrar empleados con Edad mayor a 30
print(df[df["Edad"] > 30])

# Filtrar con varias condiciones (AND y OR)
print(df[(df["Edad"] > 30) & (df["Salario"] > 60000)]) # AND
print(df[(df["Ciudad"] == "Rosario") | (df["Ciudad"] == "Salta")]) # OR

# 👉 Notá el uso obligatorio de paréntesis al combinar condiciones con & (AND) y | (OR).



# 5.4 Uso de máscaras booleanas
# Una máscara booleana es un arreglo de True/False que Pandas usa para filtrar filas de forma reutilizable.
# Crear una máscara booleana
mask = df["Edad"] > 30
print(mask)

# Aplicar la máscara al DataFrame
print(df[mask])

# Salida de la máscara:
# Nombre
# Ana False
# Luis True
# Carla False
# Pedro True
# María True
# Name: Edad, dtype: bool
# Salida del DataFrame filtrado:
# Edad Ciudad Salario
# Nombre
# Luis 35 Buenos Aires 72000
# Pedro 42 Mendoza 83000
# María 31 Salta 59000