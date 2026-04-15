# Se tiene que cargar la siguiente información:
# · Nombres de 3 empleados
# · Ingresos en concepto de sueldo, cobrado por cada empleado, en los últimos 3 meses.
# Confeccionar el programa para:
# a) Realizar la carga de los nombres de empleados y los tres sueldos por cada empleado.
# b) Generar una lista que contenga el ingreso acumulado en sueldos en los últimos 3 meses para cada empleado.
# c) Mostrar por pantalla el total pagado en sueldos a cada empleado en los últimos 3 meses
# d) Obtener el nombre del empleado que tuvo el mayor ingreso acumulado En este problema definiremos tres listas:
# Una lista para almacenar los nombres de los empleados, por ejemplo si lo cargamos por asignación:
# nombres=["juan", "ana", "luis"]
# Una lista paralela a la anterior para almacenar los sueldos en los últimos tres meses por cada empleado:
# sueldos=[[5000,5100,5000], [7000,6500,6000], [2500,2500,2500]]
# Otra lista paralela donde almacenamos el total de sueldos cobrados por cada empleado que resulta
# de sumar los tres sueldos de cada empleado contenidos en la lista sueldos:
# totalsueldos=[15100, 19500, 7500]
# Es importante notar que estos datos no los cargaremos por asignación sino los cargaremos por
# teclado a las dos primeras listas y la tercera la generaremos extrayendo los datos de la lista sueldos.

nombres=[]
sueldos=[]
totalsueldos=[]

for x in range(3):
    nom=input("Ingrese el nombre del empleado:")
    nombres.append(nom)
    su1=int(input("Ingrese el primer sueldo:"))
    su2=int(input("Ingrese el segundo sueldo:"))
    su3=int(input("Ingrese el tercer sueldo:"))
    sueldos.append([su1, su2, su3])
for x in range(3):
    total=sueldos[x][0]+sueldos[x][1]+sueldos[x][2]
    totalsueldos.append(total)
for x in range(3):
    print(nombres[x], totalsueldos[x])

posmayor=0
mayor=totalsueldos[0]
for x in range(1,3):
    if totalsueldos[x]>mayor:
        mayor=totalsueldos[x]
        posmayor=x
print("Empleado con mayores ingresos en los ultimos tres meses")
print(nombres[posmayor])
print("con un ingreso de",mayor)