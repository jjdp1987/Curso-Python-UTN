# Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8 empleados (4 por la mañana y 4 por la tarde) 
# Confeccionar un programa que permita almacenar los sueldos de los empleados agrupados en dos listas. 
# Imprimir las dos listas de sueldos.

sueldos_mañana=[]
sueldos_tarde=[]

print("Turno mañana")
for m in range(4):
    sueldo_tm = float(input(f"Ingrese el sueldo del empleado {m+1}: "))
    sueldos_mañana.append(sueldo_tm)

print("Turno tarde")
for m in range(4):
    sueldo_tt = float(input(f"Ingrese el sueldo del empleado {m+1}: "))
    sueldos_tarde.append(sueldo_tt)

print("La lista de sueldos de los empleados del turno mañana es:", sueldos_mañana)
print("La lista de sueldos de los empleados del turno tarde es:", sueldos_tarde)