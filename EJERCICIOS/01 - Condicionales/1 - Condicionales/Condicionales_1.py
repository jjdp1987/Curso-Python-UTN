# Realizar un programa que solicite la carga por teclado de dos números, si el primero es mayor al segundo informar su suma y diferencia, 
# en caso contrario informar el producto y la división del primero respecto al segundo.

a = int(input("Ingrese primer numero: "))
b = int(input("Ingrese segundo numero: "))

if a > b:
    print( "La suma es:", a + b)
    print( "La diferencia es:", a - b)
else:
    print( "El producto es:", a ** b)
    print( "La división es:", a / b)