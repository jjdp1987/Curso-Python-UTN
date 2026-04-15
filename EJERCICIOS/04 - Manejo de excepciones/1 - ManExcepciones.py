# Realizar la carga de dos números enteros por teclado e imprimir su suma, luego preguntar si quiere seguir sumando valores.
# Codificar dos programas uno que capture la excepción de ingreso de datos no numéricos y el otro
# que no tenga en cuenta el tipo de entrada de datos.

# Primero codificaremos sin la captura de excepciones.

while True:
    valor1=int(input("Ingrese primer valor:"))
    valor2=int(input("Ingrese segundo valor:"))
    suma=valor1+valor2
    print("La suma es", suma)
    respuesta=input("Desea ingresar otro par de valores?[s/n]")
    if respuesta=="n":
        break 

# Ahora la captura con excepciones.

while True:
    try:
        valor1=int(input("Ingrese primer valor:"))
        valor2=int(input("Ingrese segundo valor:"))
        suma=valor1+valor2
        print("La suma es",suma)
    except ValueError:
         print("debe ingresar números.")
         respuesta=input("Desea ingresar otro par de valores?[s/n]")
    if respuesta=="n":
        break 