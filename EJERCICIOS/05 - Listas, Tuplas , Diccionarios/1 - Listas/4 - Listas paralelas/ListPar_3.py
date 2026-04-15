# En un curso de 4 alumnos se registraron las notas de sus exámenes y se deben procesar de acuerdo a lo siguiente:
# a) Ingresar nombre y nota de cada alumno (almacenar los datos en dos listas paralelas)
# b) Realizar un listado que muestre los nombres, notas y condición del alumno. 
# En la condición, colocar "Muy Bueno" si la nota es mayor o igual a 8, "Bueno" si la nota está entre 4 y 7, y colocar "Insuficiente" si la nota es inferior a 4.
#c) Imprimir cuantos alumnos tienen la leyenda “Muy Bueno”.

alumnos = []
notas = []
condicion = []

for x in range(4):
    alumno = input(f"Ingrese el nombre del alumno {x+1}: ")
    alumnos.append(alumno)
    nota = float(input("Ingrese la nota de dicho alumno: "))
    notas.append(nota)
    if nota > 8 or nota == 8:
        condicion.append("Muy bueno")
    elif nota < 4:
        condicion.append("Insuficiente")
    else:
        condicion.append("Bueno")
    
contar = 0

print("Los alumnos que tienen condicion de Muy bueno son...")

for c in range(4):
    if condicion[c] == "Muy bueno":
        contar +=1
        print(alumnos[c])

print(f"En total son {contar} alumnos")