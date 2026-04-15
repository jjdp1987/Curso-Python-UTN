# Se ingresan por teclado tres números, si todos los valores ingresados son menores a 10,
#  imprimir en pantalla la leyenda "Todos los números son menores a diez"

n1 = int(input("Ingrese primer número: "))
n2 = int(input("Ingrese segundo número: "))
n3 = int(input("Ingrese tercer número: "))

if n1 < 10 and n2 < 10 and n3 < 10:
    print("Todos los números son menores a diez")