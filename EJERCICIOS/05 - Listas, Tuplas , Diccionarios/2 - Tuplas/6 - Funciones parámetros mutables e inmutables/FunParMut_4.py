# Crear un diccionario en Python para almacenar los datos de empleados de una empresa. La
# clave será su número de legajo y en su valor almacenar una lista con el nombre, profesión y sueldo.
# Desarrollar las siguientes funciones:
# 1) Carga de datos de empleados.
# 2) Permitir modificar el sueldo de un empleado. Ingresamos su número de legajo para buscarlo.
# 3) Mostrar todos los datos de empleados que tienen una profesión de "analista de sistemas"

def cargar():
    empleados={}
    continua="s"
    while continua=="s":
        legajo=int(input("Ingrese el numero de legajo:"))
        nombre=input("Ingrese el nombre del empleado:")
        profesion=input("Ingrese el nombre de la profesion:")
        sueldo=float(input("Ingrese el sueldo:"))
        empleados[legajo]=[nombre,profesion,sueldo]
        continua=input("Ingresa los datos de otro empleado[s/n]:")
    return empleados

def imprimir(empleados):
    print("Listado completo de empleados")
    for legajo in empleados:
        print(legajo,empleados[legajo][0],empleados[legajo][1],empleados[legajo][2])
 
def modificar_sueldo(empleados):
    legajo=int(input("Ingrese el numero de legajo para buscar empleado:"))
    if legajo in empleados:
        sueldo=float(input("Ingrese nuevo sueldo:"))
        empleados[legajo][2]=sueldo
    else:
        print("No existe un empleado con dicho numero de legajo")

def imprimir_analistas(empleados):
    print("Listado de empleados con profesion \"analista de sistemas\"")
    for legajo in empleados:
        if empleados[legajo][1]=="analista de sistemas":
            print(legajo,empleados[legajo][0],empleados[legajo][2])

# bloque principal

empleados=cargar()
imprimir(empleados)
modificar_sueldo(empleados)
imprimir(empleados)
imprimir_analistas(empleados)