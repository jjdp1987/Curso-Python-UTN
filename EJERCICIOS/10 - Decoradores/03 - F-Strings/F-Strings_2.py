# Definir una lista con 5 valores enteros. Mostrar los 5 valores formateados a derecha junto a su
# suma.
# Programa: ejercicio309.py

lista=[2000, 500, 17000, 24, 7]
for elemento in lista:
    print(f"{elemento:10}")
print("----------")
print(f"{sum(lista):10}")