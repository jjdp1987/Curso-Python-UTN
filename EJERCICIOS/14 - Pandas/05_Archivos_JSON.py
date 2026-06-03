import pandas as pd

# Ejemplo de datos.json :
# [
# {"Nombre": "Ana", "Edad": 23, "Ciudad": "Córdoba"},
# {"Nombre": "Luis", "Edad": 35, "Ciudad": "Buenos Aires"},
# {"Nombre": "Carla", "Edad": 29, "Ciudad": "Rosario"}
# ]


# Leer JSON con Pandas
df_json = pd.read_json("datos.json")
print(df_json)

# Salida:
# Nombre Edad Ciudad
# 0 Ana 23 Córdoba
# 1 Luis 35 Buenos Aires
# 2 Carla 29 Rosario


# Guardar un DataFrame en JSON
df_json.to_json("salida.json", orient="records", indent=4)