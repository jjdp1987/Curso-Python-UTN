# Se ingresan tres valores por teclado, si todos son iguales se imprime la 
# suma del primero con el segundo y a este resultado se lo multiplica por el tercero.

n1 = int(input("Ingrese primer número: "))
n2 = int(input("Ingrese segundo número: "))
n3 = int(input("Ingrese tercer número: "))

if n1 == n2 and n2 == n3:
    print((n1 + n2)*n3)