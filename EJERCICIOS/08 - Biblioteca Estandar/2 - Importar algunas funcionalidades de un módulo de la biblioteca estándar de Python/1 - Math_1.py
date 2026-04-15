# Confeccionar un programa que solicite la carga de un valor entero por teclado y luego nos muestre
# la raíz cuadrada del número y el valor elevado al cubo.
# Para resolver este problema utilizaremos dos funcionalidades que nos provee el módulo math de la
# biblioteca estándar de Python. Podemos consultar el módulo math

from math import sqrt, pow
valor=int(input("Ingrese un valor entero:"))
r1=sqrt(valor)
r2=pow(valor,3)
print("La raiz cuadrada es",r1)
print("El cubo es",r2)