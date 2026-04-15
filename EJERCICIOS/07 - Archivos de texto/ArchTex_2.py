""" Lectura de un archivo de texto """

# Leer el contenido del archivo de texto 'datos.txt'.

archi1=open("datos.txt","r")
contenido=archi1.read()
print(contenido)
archi1.close()
