# Cargar una lista con 5 elementos enteros. 
# Imprimir el mayor y un mensaje si se repite dentro de la lista (es decir si dicho valor se encuentra en 2 o más posiciones en la lista)

lista=[]

for x in range(5):
    valor=int(input(f"Ingrese el valor {x+1}: "))
    lista.append(valor)

mayor = lista[0]

for m in range(1, 5):
    if lista[m]>mayor:
        lista[m] = mayor

repeticiones = lista.count(mayor)

print(f"Lista ingresada: {lista}")
print(f"El número mayor es: {mayor}")

if repeticiones > 1:
    print(f"Aviso: El valor mayor ({mayor}) se repite {repeticiones} veces en la lista.")
else:
    print("El valor mayor no se repite.")