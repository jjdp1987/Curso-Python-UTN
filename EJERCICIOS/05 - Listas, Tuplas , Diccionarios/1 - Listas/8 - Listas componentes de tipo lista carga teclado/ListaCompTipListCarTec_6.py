# Definir una lista y almacenar los nombres de 3 empleados.
# Por otro lado definir otra lista y almacenar en cada elemento una sublista con los números de días del mes que el empleado faltó.
# Imprimir los nombres de empleados y los días que faltó.
# Mostrar los empleados con la cantidad de inasistencias.
# Finalmente mostrar el nombre o los nombres de empleados que faltaron menos días. 

# 1. Definir las listas para almacenar los datos
nombres = []
inasistencias = []

# Carga de datos para 3 empleados
for x in range(3):
    nom = input(f"Ingrese el nombre del empleado {x+1}: ")
    nombres.append(nom)
    
    cant = int(input(f"¿Cuántos días faltó {nom}?: "))
    faltas = []
    for f in range(cant):
        dia = int(input("Ingrese el número de día del mes que faltó: "))
        faltas.append(dia)
    inasistencias.append(faltas)

# 2. Imprimir los nombres de empleados y los días que faltó
print("\nListado de inasistencias detallado:")
for x in range(3):
    print(f"Empleado: {nombres[x]} - Días que faltó: {inasistencias[x]}")

# 3. Mostrar los empleados con la cantidad de inasistencias
print("\nResumen de inasistencias:")
for x in range(3):
    # Usamos len() para contar cuántos elementos hay en la sublista de faltas
    print(f"Empleado: {nombres[x]} - Total faltas: {len(inasistencias[x])}")

# 4. Mostrar el nombre o los nombres de empleados que faltaron menos días
# Primero buscamos cuál es la menor cantidad de faltas
menor_cantidad = len(inasistencias[0])
for x in range(1, 3):
    if len(inasistencias[x]) < menor_cantidad:
        menor_cantidad = len(inasistencias[x])

print(f"\nLa menor cantidad de inasistencias fue: {menor_cantidad}")
print("Empleado(s) con menos faltas:")
for x in range(3):
    if len(inasistencias[x]) == menor_cantidad:
        print(f"- {nombres[x]}")