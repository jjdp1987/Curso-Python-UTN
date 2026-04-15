# Desarrollar un programa que solicite la carga de tres valores y muestre el menor. 
# Desde el bloque principal del programa llamar 2 veces a dicha función (sin utilizar una estructura repetitiva)

def ingresar_menor():
    print("Ingrese 3 valores:")
    num1 = int(input("Ingrese el primer valor:"))
    num2 = int(input("Ingrese el segundo valor:"))
    num3 = int(input("Ingrese el tercer valor:"))
    if num1 < num2 and num1 < num3:
        print(f"El valor mas bajo es {num1}")
    elif num2 < num1 and num2 < num3:
        print(f"El valor mas bajo es {num2}")
    else:
        print(f"El valor mas bajo es {num3}")

ingresar_menor()
ingresar_menor()