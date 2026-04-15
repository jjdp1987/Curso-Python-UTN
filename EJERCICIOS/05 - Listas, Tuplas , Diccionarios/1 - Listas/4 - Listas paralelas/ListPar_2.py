# Crear y cargar dos listas con los nombres de 5 productos en una y sus respectivos precios en otra. 
# Definir dos listas paralelas. Mostrar cuantos productos tienen un precio mayor al primer producto ingresado.

productos = []
precios = []

for x in range(5):
    producto = input(f"Ingrese el nombre del producto {x+1}: ")
    productos.append(producto)
    precio = float(input("Ingrese el precio de dicho producto: "))
    precios.append(precio)

contar = 0

print(productos)

for n in range(1, 5):
    if precios[n] > precios[0]:
        print(productos[n])
