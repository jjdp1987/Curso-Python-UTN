# Elaborar una función que reciba tres enteros y nos retorne el valor promedio de los mismos.

def promedio(v1, v2, v3):
    suma = v1 + v2 + v3
    prom = int(suma / 3)
    print(f"El valor promedio es {prom}")

# Bloque principal

valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))
valor3 = int(input("Ingrese el tercer valor: "))
promedio(valor1, valor2, valor3)