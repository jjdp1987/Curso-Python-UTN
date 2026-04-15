# Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores float) Obtener el promedio de las mismas. 
# Contar cuántas personas son más altas que el promedio y cuántas más bajas.

alturas=[]

contar = 0

for x in range(5):
    valor=float(input(f"Ingrese la {x+1} estatura:"))
    alturas.append(valor)

promedio = sum(alturas) / len(alturas)

for x in range(len(alturas)):
    if alturas[x] > promedio:
        contar += 1


print(f"Lista completa de estaturas es: {alturas}")
print(f"El promedio de estaturas es: {promedio:.2f}")
print(f"El numero de personas con una estatura mayor al promedio es: {contar}")