# Crear dos listas paralelas. En la primera ingresar los nombres de empleados y en la segunda los sueldos de cada empleado.
# Ingresar por teclado cuando inicia el programa la cantidad de empleados de la empresa.
# Borrar luego todos los empleados que tienen un sueldo mayor a 10000 (tanto el sueldo como su nombre)

empleados = []
sueldos = []

cant = int(input("Ingrese el numero de empleados: "))

for k in range(cant):
    empleado = input(f"Ingrese el nombre del empleado nro {k+1}: ")
    empleados.append(empleado)
    sueldo = int(input("Ingrese su sueldo: "))
    sueldos.append(sueldo)

# Mostrar listas antes del borrado
print("\nLista original de empleados y sueldos:")
for x in range(len(empleados)):
    print(f"{empleados[x]}: ${sueldos[x]}")

# 2. Borrado de empleados con sueldo mayor a 10000
posicion = 0
while posicion < len(sueldos):
    if sueldos[posicion] > 10000:
        # Eliminamos de ambas listas para mantener la paridad
        empleados.pop(posicion)
        sueldos.pop(posicion)
        # NO incrementamos 'posicion' porque el siguiente elemento 
        # ahora ocupa el lugar del que acabamos de borrar 
    else:
        # Solo avanzamos si no hubo borrado
        posicion = posicion + 1

# 3. Mostrar resultados finales
print("\nLista final (empleados con sueldo <= 10000):")
for x in range(len(empleados)):
    print(f"{empleados[x]}: ${sueldos[x]}")