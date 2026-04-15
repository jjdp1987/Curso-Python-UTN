# Confeccionar un programa con las siguientes funciones:
# 1)Cargar una lista de 5 enteros.
# 2)Retornar el mayor y menor valor de la lista mediante una tupla.
# Desempaquetar la tupla en el bloque principal y mostrar el mayor y menor. 

def cargar():
    lista=[]
    for x in range(5):
        valor=int(input("Ingrese valor"))
        lista.append(valor)
    return lista

def retornar_mayormenor(lista):
    may=lista[0]
    men=lista[0]
    for x in range(1,len(lista)):
        if lista[x]>may:
            may=lista[x]
        else:
            if lista[x]<men:
             men=lista[x]
    return(may,men)
    
# bloque principal

lista=cargar()
mayor,menor=retornar_mayormenor(lista)
print("Mayor valor de la lista:",mayor)
print("Menor valor de la lists:",menor)