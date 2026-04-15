# Conectarse a una base de datos de MySQL y ejecutar un comando SQL incorrecto

#import mysql.connector
#try:
#    conexion1=mysql.connector.connect(host="localhost", user="root", passwd="")
#    cursor1=conexion1.cursor()
#    cursor1.execute("show databasesqqqqqqqq")
#    for base in cursor1:
#        print(base)
#except mysql.connector.errors.ProgrammingError:
#    print("Error en el comando SQL")
#finally:
#    conexion1.close()
#    print("Se cerró la conexión a la base de datos")

# Hemos definido un comando SQL incorrecto al llamar al método 'execute':
#  cursor1.execute("show databasesqqqqqqqq")
# Luego se captura la excepción 'ProgrammingError' que se encuentra en el módulo
# 'mysql.connector.errors':
# except mysql.connector.errors.ProgrammingError:
#  print("Error en el comando SQL")
# Indistintamente que dispongamos un comando SQL correcto o incorrecto luego se ejecuta el bloque
# finally donde cerramos la conexión:
# finally:
#  conexion1.close()
#  print("Se cerró la conexión a la base de datos")