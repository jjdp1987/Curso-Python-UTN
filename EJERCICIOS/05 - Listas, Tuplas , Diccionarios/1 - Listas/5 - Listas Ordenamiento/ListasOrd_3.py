# Crear una lista y almacenar los nombres de 5 países. 
# Ordenar alfabéticamente la lista e imprimirla.

paises = []

for x in range(5):
    pais = input(f"Ingresar el pais {x+1}: ")
    paises.append(pais)

print(f"La lista ingresada es la siguiente: {paises}")

for k in range(4):
    for n in range(4):
        if paises[n] > paises[n+1]:
            aux = paises[n]
            paises[n] = paises[n+1]
            paises[n+1] = aux

print("La lista ordenada es", paises)
