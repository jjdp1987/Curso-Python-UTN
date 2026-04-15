# Crear y cargar una lista con los nombres de tres alumnos. Cada alumno tiene dos notas, almacenar las notas en una lista paralela. 
# Cada componente de la lista paralela debe ser también una lista con las dos notas. Imprimir luego cada nombre y sus dos notas.

alumnos=["juan", "ana", "luis"]
notas=[[10,8], [6,5], [2,8]]

nombres=[]
notas=[]
for x in range(3):
    nom=input("Ingrese el nombre del alumno:")
    nombres.append(nom)
    no1=int(input("Ingrese la primer nota:"))
    no2=int(input("Ingrese la segunda nota:"))
    notas.append([no1,no2])
for x in range(3):
    print(nombres[x],notas[x][0],notas[x][1])