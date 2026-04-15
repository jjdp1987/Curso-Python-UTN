""" Creación de un archivo de texto y almacenamiento de datos """

# Crear un archivo de texto llamado 'datos.txt', almacenar tres líneas de texto. 
# Abrir luego el archivo creado con un editor de texto.

archi1=open("datos.txt","w")
archi1.write("Primer línea.\n")
archi1.write("Segunda línea.\n")
archi1.write("Tercer línea.\n")
archi1.close() 