# Almacenar los nombres de 5 productos y sus precios. Utilizar una lista y cada elemento una tupla con el nombre y el precio.
# Desarrollar las funciones:
# 1) Cargar por teclado.
# 2) Listar los productos y precios.
# 3) Imprimir los productos con precios comprendidos entre 10 y 15. 

def cargar():
    productos=[]
    for x in range(5):
        nombre=input("Ingrese el nombre del producto:")
        precio=int(input("Ingrese el precio:"))
        productos.append((nombre,precio))
    return productos

def imprimir(productos):
    print("Listado de productos y precios")
    for nombre,precio in productos:
        print(nombre,precio)

def imprimir_entre10y15(productos):
    print("Listado de productos que tienen un precio comprendido entre 10 y 15")
    for nombre,precio in productos:
        if precio>=10 and precio<=15:
            print(nombre,precio)

# bloque principal
productos=cargar()
imprimir(productos)
imprimir_entre10y15(productos)