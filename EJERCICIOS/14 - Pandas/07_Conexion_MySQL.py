# Necesitamos instalar:
# pip install sqlalchemy pymysql
# SQLAlchemy: biblioteca para trabajar con SQL en Python.
# PyMySQL: conector específico para MySQL.
# Conexión a MySQL y lectura de datos

import pandas as pd
from sqlalchemy import create_engine

# Crear la conexión a MySQL
usuario = "root"
contrasena = "mi_password"
host = "localhost"
base_datos = "mi_base"

# Cadena de conexión
conexion = create_engine(f"mysql+pymysql://{usuario}:{contrasena}@{host}/{base_datos}")

# Leer datos desde una tabla
df_mysql = pd.read_sql("SELECT * FROM usuarios", conexion)
print(df_mysql.head())


# Guardar un DataFrame en MySQL
# Guardar un DataFrame en una tabla MySQL
df.to_sql("nueva_tabla", conexion, if_exists="replace", index=False)
# Parámetros importantes:
if_exists="replace" #: reemplaza la tabla si ya existe.
if_exists="append" #: agrega los datos al final de la tabla existente.
# Diferencias con SQLite
# SQLite se guarda en un archivo ( .db ), mientras que MySQL requiere un servidor activo.
# MySQL permite múltiples usuarios, mayor escalabilidad y soporte para proyectos grandes.
# Con Pandas, la forma de trabajar es casi idéntica: solo cambia la cadena de conexión.
# Con esto, ya tenés una conexión profesional y escalable entre Pandas y MySQL, lista para proyectos reales de
# ciencia de datos.