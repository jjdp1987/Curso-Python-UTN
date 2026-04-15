# Realizar un programa que lea los lados de n triángulos, e informar:
# a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados
# iguales), isósceles (dos lados iguales), o escaleno (ningún lado igual)
# b) Cantidad de triángulos de cada tipo.

n = int(input("Ingrese la cantidad de triángulos que desea cargar: "))

equilatero = 0
isosceles = 0
escaleno = 0

for vuelta in range(n):
    a = int(input("Ingrese el 1er lado: "))
    b = int(input("Ingrese el 2do lado: "))
    c = int(input("Ingrese el 3er lado: "))
    if a == b and b == c:
        triangulo = "Equilátero"
        equilatero += 1
    elif a == b or a == c or b == c:
        triangulo = "Isósceles"
        isosceles += 1
    else:
        triangulo = "Escaleno"
        escaleno += 1

    print(f"El triángulo es: {triangulo}")

print(f"El total de triangulos es, triangulos equilateros: {equilatero} , triangulos isosceles: {isosceles}  y triangulos escalenos: {escaleno} ")