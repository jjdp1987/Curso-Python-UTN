# Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio de las personas. 

n = int(input("Ingrese el nro de alturas a ingresar: "))
contador = 1
acumulador = 0

while contador <= n:
    alt = float(input("Ingrese la altura: "))
    acumulador = acumulador + alt
    
    contador += 1

promedio = acumulador / n

print(promedio)
print(acumulador)