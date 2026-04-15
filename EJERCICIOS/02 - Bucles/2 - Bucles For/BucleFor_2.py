# Desarrollar un programa que solicite la carga de 10 números e imprima la
# suma de los últimos 5 valores ingresados.

suma = 0

for x in range(10):
    valor = int(input("Ingrese valor:"))
    if x >4:
        suma += valor

print("La suma de los últimos 5 valores ingresados es:", suma)