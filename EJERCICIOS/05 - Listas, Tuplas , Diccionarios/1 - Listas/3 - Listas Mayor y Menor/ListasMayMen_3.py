# Ingresar por teclado los nombres de 5 personas y almacenarlos en una lista. 
# Mostrar el nombre de persona menor en orden alfabético.

nombres=[]

menor = 0 
for x in range(5):
    Nom=input(f"Ingrese el nombre {x+1}: ")
    nombres.append(Nom)

menor=nombres[0]

for n in range(1,5):
    if nombres[n]<menor:
        menor=nombres[n]

print(menor)
