# Confeccionar una función que calcule la superficie de un rectángulo y la retorne, la función
# recibe como parámetros los valores de dos de sus lados:

#def retornar_superficie(lado1,lado2):

# En el bloque principal del programa cargar los lados de dos rectángulos y luego mostrar cual
# de los dos tiene una superficie mayor.

def mensaje(texto):
    print("============================================================")
    print(texto)
    print("============================================================")

def retornar_superficie(lado1,lado2):
    sup = lado1 * lado2
    return sup

# Bloque principal

mensaje("Primer rectángulo")
l1 = int(input("Ingrese el primer lado: "))
l2 = int(input("Ingrese el segundo lado: "))

mensaje("segundo rectángulo")
l3 = int(input("Ingrese el primer lado: "))
l4 = int(input("Ingrese el segundo lado: "))

mensaje("Resultado")

if retornar_superficie(l1, l2) > retornar_superficie(l3, l4):
    print(f"El primer rectángulo tiene una superficie mayor con {retornar_superficie(l1, l2)}")
else:
    print(f"El segundo rectángulo tiene una superficie mayor con {retornar_superficie(l3, l4)}")