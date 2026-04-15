# Confeccionar un programa que permita cargar un número entero positivo de hasta tres cifras y muestre un mensaje indicando
#  si tiene 1, 2, o 3 cifras. Mostrar un mensaje de error si el número de cifras es mayor.

x = int(input("Ingrese un número entero positivo de hasta tres cifras: "))

if x >= 0 and x < 10:
    print("El numero ingresado tiene 1 dígito")
elif x >= 10 and x < 100:
    print("El numero ingresado tiene 2 dígito")
elif x >= 100 and x < 1000:
    print("El numero ingresado tiene 3 dígito")
elif x >= 1000:
    print("Error")
else:
    print("El numero ingresado es negativo")