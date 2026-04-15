# Se desea saber la temperatura media trimestral de cuatro paises. Para ello se tiene como dato
# las temperaturas medias mensuales de dichos paises.
# Se debe ingresar el nombre del país y seguidamente las tres temperaturas medias mensuales.
# Seleccionar las estructuras de datos adecuadas para el almacenamiento de los datos en memoria.
# a - Cargar por teclado los nombres de los paises y las temperaturas medias mensuales.
# b - Imprimir los nombres de las paises y las temperaturas medias mensuales de las mismas.
# c - Calcular la temperatura media trimestral de cada país.
# c - Imprimir los nombres de los paises y las temperaturas medias trimestrales.
# b - Imprimir el nombre del pais con la temperatura media trimestral mayor.

paises = []
temperaturas = []
promedios = []

# a - Cargar por teclado los nombres de los paises y las temperaturas
for x in range(4):
    nom = input(f"Ingrese el nombre del país {x+1}: ")
    paises.append(nom)
    temp1 = float(input("Ingrese la temperatura del primer mes: "))
    temp2 = float(input("Ingrese la temperatura del segundo mes: "))
    temp3 = float(input("Ingrese la temperatura del tercer mes: "))
    # Almacenamos las tres temperaturas como una lista anidada
    temperaturas.append([temp1, temp2, temp3])

# b - Imprimir los nombres y las temperaturas mensuales
print("\nTemperaturas mensuales registradas:")
for x in range(4):
    print(f"País: {paises[x]} - Temperaturas: {temperaturas[x][0]}, {temperaturas[x][1]}, {temperaturas[x][2]}")

# c - Calcular e imprimir la temperatura media trimestral de cada país
print("\nTemperaturas medias trimestrales:")
for x in range(4):
    # Sumamos los componentes de la sublista y dividimos por 3
    suma = temperaturas[x][0] + temperaturas[x][1] + temperaturas[x][2]
    promedio = suma / 3
    promedios.append(promedio)
    print(f"País: {paises[x]} - Promedio Trimestral: {promedio:.2f}")

# d - Imprimir el nombre del pais con la temperatura media trimestral mayor
posmayor = 0
mayor = promedios[0]
for x in range(1, 4):
    if promedios[x] > mayor:
        mayor = promedios[x]
        posmayor = x

print(f"\nEl país con la mayor temperatura media es {paises[posmayor]} con {mayor:.2f}")