# Solicitar por teclado la cantidad de empleados que tiene la empresa. 
# Crear y cargar una lista con todos los sueldos de dichos empleados. 
# Imprimir la lista de sueldos ordenamos de menor a mayor.

sueldos = []

n = int(input("Ingrese la cantidad de empleados: "))

for x in range(n):
    sueldo = float(input(f"Ingrese el sueldo del empleado nro {x+1}: "))
    sueldos.append(sueldo)

for k in range(n-1):
    for i in range(n-1):
        if sueldos[i] > sueldos[i+1]:
            aux = sueldos[i]
            sueldos[i] = sueldos[i+1]
            sueldos[i+1] = aux

print(f"La lista de sueldos ordenada de menor a mayor es {sueldos}")