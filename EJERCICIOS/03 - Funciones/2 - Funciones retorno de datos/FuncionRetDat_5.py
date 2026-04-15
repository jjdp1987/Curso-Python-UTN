# Elaborar una función que nos retorne el perímetro de un cuadrado pasando como parámetros el valor de un lado.

def perimetro(lado):
    peri = lado * 4
    return peri

# Bloque principal

lad = int(input("Ingrese el valor del lado del cuadrado: "))
print(f"El valor del perimetro del cuadrado es {perimetro(lad)}")