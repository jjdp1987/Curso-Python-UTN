# Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
#a) La cantidad de valores ingresados negativos.
#b) La cantidad de valores ingresados positivos.
#c) La cantidad de múltiplos de 15.
#d) El valor acumulado de los números ingresados que son pares.

negativos = 0
positivos = 0
multiplos_15 = 0
suma_pares = 0

for vuelta in range(10):
    valor = int(input("Ingrese un numero entero: "))
    if valor < 0:
        negativos += 1
    elif valor >= 0:
        positivos += 1
    
    if valor % 15 == 0:
        multiplos_15 += 1
    
    if valor % 2 == 0:
        suma_pares += valor

print("Cantidad de valores ingresados negativos:", negativos)
print("Cantidad de valores ingresados positivos:", positivos)
print("Cantidad de múltiplos de 15:", multiplos_15)
print("Valor acumulado de los números ingresados que son pares:", suma_pares)