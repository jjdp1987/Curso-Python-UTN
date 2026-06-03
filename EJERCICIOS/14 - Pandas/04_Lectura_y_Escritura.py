import pandas as pd

# Leer un CSV
df = pd.read_csv("datos.csv")
print(df.head())

# Ejemplo de datos.csv :
# Nombre,Edad,Ciudad
# Ana,23,Córdoba
# Luis,35,Buenos Aires
# Carla,29,Rosario
# Pedro,42,Mendoza

# Salida:
# Nombre Edad Ciudad
# 0 Ana 23 Córdoba
# 1 Luis 35 Buenos Aires
# 2 Carla 29 Rosario
# 3 Pedro 42 Mendoza

# Leer un archivo TSV (Tab Separated Values)
# Un archivo TSV (Valores Separados por Tabulaciones) es un archivo de texto plano que almacena datos tabulares
# donde cada fila representa un registro y los valores de cada columna están separados por caracteres de tabulación
# en lugar de comas.

df_tsv = pd.read_csv("datos.tsv", sep="\t")
print(df_tsv.head())

# Leer archivos de texto plano
df_txt = pd.read_csv("datos.txt", sep=";")
print(df_txt.head())

# Guardar un DataFrame en CSV
# Guardar en CSV
df.to_csv("salida.csv", index=False) # index=False evita guardar la columna de índices


#EXCEL
# Leer hoja por defecto
df_excel = pd.read_excel("datos.xlsx")
print(df_excel.head())
# Leer una hoja específica
df_hoja = pd.read_excel("datos.xlsx", sheet_name="Hoja1")

# Guardar un DataFrame en Excel
df.to_excel("salida.xlsx", sheet_name="Resultados", index=False)