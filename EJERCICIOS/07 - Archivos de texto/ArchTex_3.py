""" Lectura de un archivo de texto línea a línea """

# Leer el contenido del archivo de texto 'datos.txt' línea a línea.

archi1=open("datos.txt","r")
linea=archi1.readline()
while linea!='':
    print(linea, end='')
    linea=archi1.readline()
archi1.close()

# También dentro de la estructura while leemos las siguientes líneas.
# Podemos recorrer el archivo leyendo línea a línea utilizando la estructura repetitiva for:

archi1=open("datos.txt","r")
for linea in archi1:
    print(linea, end='')
archi1.close()
