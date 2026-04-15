# Se cuenta con la siguiente información:
# Las edades de 5 estudiantes del turno mañana.
# Las edades de 6 estudiantes del turno tarde.
# Las edades de 11 estudiantes del turno noche.
# Las edades de cada estudiante deben ingresarse por teclado.
# a) Obtener el promedio de las edades de cada turno (tres promedios)
# b) Imprimir dichos promedios (promedio de cada turno)
# c) Mostrar por pantalla un mensaje que indique cual de los tres turnos tiene un
#    promedio de edades mayor.

turno_mañana = 0
turno_tarde = 0
turno_noche = 0


for tm in range(5):
    alum1 = int(input("Ingrese la edad del estudiante de turno mañana: "))
    turno_mañana += alum1

for tt in range(6):
    alum2 = int(input("Ingrese la edad del estudiante de turno tarde: "))
    turno_tarde += alum2

for tn in range(11):
    alum3 = int(input("Ingrese la edad del estudiante de turno noche: "))
    turno_noche += alum3

promedio_tm = turno_mañana / 5
promedio_tt = turno_tarde / 6
promedio_tn = turno_noche / 11

print(f"El promedio de edad dl turno mañana es de: {promedio_tm}")
print(f"El promedio de edad dl turno tarde es de: {promedio_tt}")
print(f"El promedio de edad dl turno noche es de: {promedio_tn}")

if promedio_tm > promedio_tt and promedio_tm > promedio_tn:
    print("El turno mañana tiene el mayor promedio de edades.")
elif promedio_tt > promedio_tm and promedio_tt > promedio_tn:
    print("El turno tarde tiene el mayor promedio de edades.")
else:
    print("El turno noche tiene el mayor promedio de edades.")