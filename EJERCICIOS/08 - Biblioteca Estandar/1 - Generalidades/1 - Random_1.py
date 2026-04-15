# Confeccionar un programa que simule tirar dos dados y luego muestre los valores que salieron.
# Imprimir un mensaje que ganó si la suma de los mismos es igual a 7.
# Para resolver este problema requerimos un algoritmo para que se genere un valor aleatorio entre 1 y # 6. 
# Como la generación de valores aleatorios es un tema muy frecuente la biblioteca estándar de
# Python incluye un módulo que nos resuelve la generación de valores aleatorios.


import random
dado1=random.randint(1,6)
dado2=random.randint(1,6)
print("Primer dado:",dado1)
print("Segundo dado:",dado2)
suma=dado1+dado2
if suma==7:
    print("Gano")
else:
    print("Perdio")

    # randint genera un ramdom entero entre los datos del parametro, en este caso entre 1 y 6, simulando el lanzamiento de un dado. 
    # Luego se suman los resultados de ambos dados y se verifica si la suma es igual a 7 para determinar si se ganó o perdió.

    # Si pongo random.random lo hace con Float extensos
    # Si pongo random.uniform (1.0, 6.0) Lo hace desde float con ese rango
    # Si pongo round(random.uniform (1.0, 6.0), 2) Lo hace desde float con ese rango restrinjo a 2 decimales
