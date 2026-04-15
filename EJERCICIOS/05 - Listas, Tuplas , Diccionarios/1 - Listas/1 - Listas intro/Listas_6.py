# Definir una lista que almacene por asignación los nombres de 5 personas. Contar cuantos de
# esos nombres tienen 5 o más caracteres. 

lista = ["juan", "pedro", "gabriel", "ana", "jose"]

contar = 0

for x in range(len(lista)):
    if len(lista[x]) > 5:
        contar += 1

print(f"La cantidad de nombres con más de 5 letras es {contar}")