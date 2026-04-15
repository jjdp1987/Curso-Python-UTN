# Se ingresa por teclado un valor entero, mostrar una leyenda que indique si el número es positivo, negativo o nulo (es decir cero) 

x = int(input("Ingrese un numero entero: "))

if x > 0:
    print("El numero ingresado es positivo")
elif x < 0:
    print("El numero ingresado en negativo")
else:
    print("El numero ingresado es nulo")