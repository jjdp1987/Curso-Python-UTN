# Almacenar en una lista los sueldos (valores float) de 5 operarios. Imprimir la lista y el promedio de sueldos.

sueldos=[]

for x in range(5):
    valor=float(input("Ingrese sueldo:"))
    sueldos.append(valor)

promedio = sum(sueldos) / len(sueldos)

print(f"Lista completa de sueldos: {sueldos}")
print(f"El promedio de los sueldos es: {promedio:.2f}")