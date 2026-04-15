# Definir una lista vacía y luego solicitar la carga de 5 enteros por teclado y añadirlos a la lista.
# Imprimir la lista generada.

#definimos una lista vacia

lista=[]

#disponemos un ciclo de 5 vueltas

for x in range(5):
    valor=int(input("Ingrese un valor entero:"))
    lista.append(valor)

#imprimimos la lista

print(lista)