# Pandas permite leer y escribir directamente desde bases de datos relacionales como MySQL, PostgreSQL o SQLite,
# generalmente en conjunto con SQLAlchemy.
# Ejemplo con SQLite
import sqlite3
import pandas as pd

# Conexión a base SQLite
conexion = sqlite3.connect("mibase.db")

# Crear un DataFrame con algunos datos de prueba
data = {
"nombre": ["Juan", "María", "Pedro", "Ana"],
"edad": [25, 30, 35, 28],
"ciudad": ["Madrid", "Barcelona", "Sevilla", "Valencia"]
} 
df = pd.DataFrame(data)

# Guardar un DataFrame en la base de datos
df.to_sql("personas", conexion, if_exists="replace", index=False)
print("\nDataFrame guardado en la base de datos 'mibase.db' en la tabla 'personas'.")

# Leer los datos de la base de datos y guardarlos en otro DataFrame
df_leido = pd.read_sql("SELECT * FROM personas", conexion)
print("\nDataFrame leído de la base de datos:")
print(df_leido)

# Cerrar la conexión
conexion.close()
print("\nConexión a la base de datos cerrada.")