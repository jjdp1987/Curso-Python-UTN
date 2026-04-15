# Se ingresa por teclado un número positivo de uno o dos dígitos (1..99) mostrar un mensaje indicando si el número tiene uno o dos dígitos. 
# (Tener en cuenta que condición debe cumplirse para tener dos dígitos un número entero)

x = int(input("Ingrese un numero positivo de 1 o 2 digitos: "))

if x >= 0 and x < 10:
    print("El numero tiene 1 digito")
elif x >= 10 and x < 100:
    print("El numero tiene 2 digitos")
else:
    print("El numero ingresado no es positivo o tiene más de 2 dígitos")