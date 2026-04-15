# Confeccionar un programa que lea n pares de datos, cada par de datos
# corresponde a la medida de la base y la altura de un triángulo. El programa
# deberá informar:
# a) De cada triángulo la medida de su base, su altura y su superficie.
# b) La cantidad de triángulos cuya superficie es mayor a 12.

n = int(input("Cuántos triángulos procesará: "))
cantidad = 0

for x in range(n):

    altura = float(input("Ingrese la altura del triángulo: "))
    base = float(input("Ingrese la base del triángulo: "))
    superficie = (base * altura) / 2
    print("La superficie del triángulo es: ", superficie)
    
    if superficie > 12:
        cantidad += 1

print("Cantidad de triángulos con superficie mayor a 12:", cantidad)