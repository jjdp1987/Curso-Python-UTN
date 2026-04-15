# Se desea almacenar los datos de 3 alumnos. Definir un diccionario cuya clave sea el número
# de documento del alumno. Como valor almacenar una lista con componentes de tipo tupla
# donde almacenamos nombre de materia y su nota.
# Crear las siguientes funciones:
# 1) Carga de los alumnos (de cada alumno solicitar su dni y los nombres de las materias y sus notas)
# 2) Listado de todos los alumnos con sus notas
# 3) Consulta de un alumno por su dni, mostrar las materias que cursa y sus notas.


def cargar():
    alumnos={}
    for x in range(3):
        dni=int(input("Ingrese el numero de dni:"))
        listamaterias=[]
        continua="s"
        while continua=="s":
            materia=input("Ingrese el nombre de materia que cursa:")
            nota=int(input("Ingrese la nota:"))
            listamaterias.append((materia,nota))
            continua=input("Desea cargar otra materia para dicho alumno [s/n}:")
            alumnos[dni]=listamaterias
    return alumnos

def listar(alumnos):
    for dni in alumnos:
        print("Dni del alumno",dni)
        print("Materias que cursa y notas")
    for nota,materia in alumnos[dni]:
        print(materia,nota)

def consulta_notas(alumnos):
    dni=int(input("Ingrese el dni a consultar:"))
    if dni in alumnos:
        for nota,materia in alumnos[dni]:
            print(materia,nota)

# bloque principal

alumnos=cargar()
listar(alumnos)
consulta_notas(alumnos) 