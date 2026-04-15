# Realizar un programa que pida la carga de dos listas numéricas enteras de 4 elementos cada una. 
# Generar una tercer lista que surja de la suma de los elementos de la misma posición de cada lista. 
# Mostrar esta tercer lista.

lista1 = []
lista2 = []
lista3 = []

for x in range(4):
    num1 = int(input(f"Ingrese el numero {x+1} de la primer lista: "))
    lista1.append(num1)
    num2 = int(input(f"Ingrese el numero {x+1} de la segunda lista: "))
    lista2.append(num2)
    lista3.append(num1 + num2)

print("La suma de ambos numeros es: ", lista3)