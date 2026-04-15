# Se ingresan por teclado tres números, si al menos uno de los valores ingresados 
# es menor a 10, imprimir en pantalla la leyenda "Alguno de los números es menor a diez".

n1 = int(input("Ingrese primer número: "))
n2 = int(input("Ingrese segundo número: "))
n3 = int(input("Ingrese tercer número: "))

if n1 < 10 or n2 < 10 or n3 < 10:
    print("Alguno de los números es menor a diez")