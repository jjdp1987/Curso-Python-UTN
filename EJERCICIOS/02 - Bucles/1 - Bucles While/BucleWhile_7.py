# Desarrollar un programa que permita cargar n números enteros y luego nos informe cuántos valores fueron pares 
# y cuántos impares. Emplear el operador “%” en la condición de la estructura condicional (este operador 
# retorna el resto de la división de dos valores, por ejemplo 11%2 retorna un 1):

n = int(input("Ingrese la cantidad de números enteros que desea cargar: ")) 
x = 1
par = 0
impar = 0

while x <= n:
    valor = int(input("Ingrese número: "))
    if (valor % 2) == 0:
        par += 1
    else:
        impar += 1

    x += 1

print(f"La cantidad de números pares es {par} y la cantidad de números impares es {impar}")