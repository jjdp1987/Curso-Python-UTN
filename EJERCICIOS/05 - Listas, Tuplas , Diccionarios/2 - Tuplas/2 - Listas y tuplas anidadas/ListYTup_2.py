# Almacenar en una lista 5 empleados, cada elemento de la lista es una sub lista con el nombre
# del empleado junto a sus últimos tres sueldos (estos tres valores en una tupla)
# El programa debe tener las siguientes funciones:
# 1)Carga de los nombres de empleados y sus últimos tres sueldos.
# 2)Imprimir el monto total cobrado por cada empleado.
# 3)Imprimir los nombres de empleados que tuvieron un ingreso trimestral mayor a 10000 en
# los últimos tres meses.
# Tener en cuenta que la estructura de datos si se carga por asignación debería ser similar a:
# empleados = [["juan",(2000,3000,4233)] , ["ana",(3444,1000,5333)] , etc.]

def cargar_empleados():
    empleados=[]
    for x in range(5):
        nom=input("Ingrese el nombre del empleado:")
        su1=int(input("Primer sueldo:"))
        su2=int(input("Segundo sueldo:"))
        su3=int(input("Tercer sueldo:"))
        empleados.append([nom,(su1,su2,su3)])
    return empleados

def ganancias(empleados):
    print("Monto total ganado por empleado en los ultimos tres meses")
    for x in range(5):
        total=empleados[x][1][0]+empleados[x][1][1]+empleados[x][1][2]
    print(empleados[x][0],total)

def ganancias_superior10000(empleados):
    print("Empleados con ingresos superiores a 10000 en los ultimos 3 meses")
    for x in range(5):
        total=empleados[x][1][0]+empleados[x][1][1]+empleados[x][1][2]
        if total>10000:
            print(empleados[x][0],total)

# bloque principal
empleados=cargar_empleados()
ganancias(empleados)
ganancias_superior10000(empleados) 