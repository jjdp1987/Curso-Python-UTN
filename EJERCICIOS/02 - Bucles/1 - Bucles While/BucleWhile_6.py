# Realizar un programa que permita cargar dos listas de 15 valores cada una. Informar con un mensaje cual de
#  las dos listas tiene un valor acumulado mayor (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")
#  Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo.

list_1 = 1
acum_1 = 0
list_2 = 1
acum_2 = 0


while list_1 <= 15:
    dato_1 = int(input("Ingrese el valor de la primer lista: "))
    acum_1 += dato_1

    list_1 += 1

while list_2 <= 15:
    dato_2 = int(input("Ingrese el valor de la segunda lista: "))
    acum_2 += dato_2

    list_2 += 1

if acum_1 > acum_2:
    print("La lista 1 es mayor a la lista 2")
elif acum_1 < acum_2:
    print("La lista 2 es mayor que la lista 1")
else:
    print("Las listas son iguales")