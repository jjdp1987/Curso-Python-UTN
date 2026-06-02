# 1.3 Primer programa con Pandas
# Una vez instalado, se importa con la convención estándar:
import pandas as pd
# Crear una Serie (columna de datos)
serie = pd.Series([10, 20, 30, 40, 50])
print("Serie:")
print(serie)
# Crear un DataFrame (tabla)
datos = {
"Nombre": ["Ana", "Luis", "Carla", "Pedro"],
"Edad": [23, 35, 29, 42],
"Ciudad": ["Córdoba", "Buenos Aires", "Rosario", "Mendoza"]
} 
df = pd.DataFrame(datos)
print("\nDataFrame:")
print(df)
# Salida esperada:
# Serie:
# 0 10
# 1 20
# 2 30
# 3 40
# 4 50
# dtype: int64
# DataFrame:
# Nombre Edad Ciudad
# 0 Ana 23 Córdoba
# 1 Luis 35 Buenos Aires
# 2 Carla 29 Rosario
# 3 Pedro 42 Mendoza