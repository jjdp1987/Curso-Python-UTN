""" Abrir un archivo para leer y agregar datos """

# Abrir un archivo de texto con el parámetro "r+", imprimir su contenido actual y
# agregar luego dos líneas al final.

archi1=open("datos.txt","r+")
contenido=archi1.read()
print(contenido)
archi1.write("Otra línea 1\n")
archi1.write("Otra línea 2\n")
archi1.close()
