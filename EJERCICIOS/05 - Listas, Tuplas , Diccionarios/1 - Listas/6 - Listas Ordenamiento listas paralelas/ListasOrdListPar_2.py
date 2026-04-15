# Crear y cargar en un lista los nombres de 5 países y en otra lista paralela la cantidad de habitantes del mismo. 
# Ordenar alfabéticamente e imprimir los resultados. 
# Por último ordenar con respecto a la cantidad de habitantes (de mayor a menor) e imprimir nuevamente.

paises = []
habitantes = []

for x in range(5):
    pais = input(f"Ingrese el nombre del pais {x+1}: ")
    paises.append(pais)
    poblacion = int(input(f"Ingrese el numero de habitantes de {pais}: "))
    habitantes.append(poblacion)

# --- CORRECCIÓN AQUÍ: Ordenamiento Alfabético ---
for k in range(4):
    for x in range(4 - k): # Agregamos el segundo bucle
        if paises[x] > paises[x+1]:
            # Intercambiamos PAÍSES
            aux1 = paises[x]
            paises[x] = paises[x+1]
            paises[x+1] = aux1
            # ¡CRUCIAL!: También debemos intercambiar HABITANTES aquí
            aux_h = habitantes[x]
            habitantes[x] = habitantes[x+1]
            habitantes[x+1] = aux_h

print(f"Orden alfabético: {paises}")
print(f"Habitantes sincronizados: {habitantes}")

# --- SEGUNDO ORDENAMIENTO (Por población) ---
# Este lo tenías casi perfecto, solo ajustamos el rango por eficiencia
for a in range(4):
    for b in range(4 - a): 
        if habitantes[b] < habitantes[b+1]:
            # Intercambiamos habitantes
            aux2 = habitantes[b]
            habitantes[b] = habitantes[b+1]
            habitantes[b+1] = aux2
            # Intercambiamos países
            aux3 = paises[b]
            paises[b] = paises[b+1]
            paises[b+1] = aux3

print("Orden por población (mayor a menor):")
for i in range(5):
    print(f"{paises[i]}: {habitantes[i]}")
