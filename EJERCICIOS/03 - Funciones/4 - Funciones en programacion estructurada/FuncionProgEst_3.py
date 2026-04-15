# Desarrollar un programa con dos funciones. La primer solicite el ingreso de un entero y
# muestre el cuadrado de dicho valor. La segunda que solicite la carga de dos valores y
# muestre el producto de los mismos. LLamar desde el bloque del programa principal a ambas funciones.

def cuadrado():
    print("Ingrese un numero y se calculara su cuadrado")
    num1 = int(input("Ingrese un número entero:"))
    cuad = num1 ** 2
    print(f"El cuadrado de {num1} es {cuad}")

def productos():
    print("Ingrese dos numeros y se calculará el producto")
    num2 = int(input("Ingrese el primer numero:"))
    num3 = int(input("Ingrese el segundo numero:"))
    prod = num2 // num3
    print(f"El producto de {num2} y {num3} es {prod}")

# Programa principal

cuadrado()
productos()