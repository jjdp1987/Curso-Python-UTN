# Escribir un programa que pida ingresar coordenadas (x,y) que representan
# puntos en el plano.
# Informar cuántos puntos se han ingresado en el primer, segundo, tercer y
# cuarto cuadrante. Al comenzar el programa se pide que se ingrese la cantidad
# de puntos a procesar.

n = int(input("Ingrese la cantidad de puntos con los que desea trabajar: "))

cuadrante_1 = 0
cuadrante_2 = 0
cuadrante_3 = 0
cuadrante_4 = 0

for vuelta in range(n):
    x = float(input("Ingrese la coordenada x: "))
    y = float(input("Ingrese la coordenada y: "))
    if x < 0 and y > 0:
        cuadrante_1 += 1
    elif x > 0 and y > 0:
        cuadrante_2 += 1
    elif x < 0 and y < 0:
        cuadrante_3 += 1
    else:
        cuadrante_4 += 1

print("Puntos en el primer cuadrante:", cuadrante_1)
print("Puntos en el segundo cuadrante:", cuadrante_2)
print("Puntos en el tercer cuadrante:", cuadrante_3)
print("Puntos en el cuarto cuadrante:", cuadrante_4)