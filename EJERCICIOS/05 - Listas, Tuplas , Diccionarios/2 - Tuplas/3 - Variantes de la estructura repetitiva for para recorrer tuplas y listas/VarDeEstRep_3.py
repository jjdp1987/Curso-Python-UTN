# Definir una función que cargue una lista con palabras y la retorne.
# Luego otra función tiene que mostrar todas las palabras de la lista que tienen más de 5 caracteres. 

def cargar():
    palabras=[]
    cant=int(input("Cuantas palabras quiere cargar?"))
    for x in range(cant):
        pal=input("Ingrese palabra:")
        palabras.append(pal)
    return palabras

def palabras_mas5(palabras):
    print("Palabras ingresadas con mas de 5 caracteres")
    for palabra in palabras:
        if len(palabra)>5:
            print(palabra)

# bloque principal
palabras=cargar()
palabras_mas5(palabras)
