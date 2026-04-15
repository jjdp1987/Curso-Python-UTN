# Confeccionar un programa que almacene en un diccionario como clave el nombre de un contacto y como valor su número telefónico:
# 1) Carga de contactos y su número telefónico.
# 2) Pemitir modificar el número telefónico. Se ingresa el nombre del contacto para su búsqueda.
# 3) Imprimir la lista completa de contactos con sus números telefónicos.

def cargar():
    contactos={}
    continua="s"
    while continua=="s":
        nombre=input("Ingrese el nombre del contacto:")
        telefono=input("Ingrese el numero de telefono:")
        contactos[nombre]=telefono
        continua=input("Ingresa otro contacto[s/n]?:")
    return contactos

def modificar_telefono(contactos):
    nombre=input("Ingrese el nombre de contacto a modificar el telefono:")
    if nombre in contactos:
        telefono=input("Ingrese el nuevo numero telefonico")
        contactos[nombre]=telefono
    else:
        print("No existe un contacto con el nombre ingresado")

def imprimir(contactos):
    print("Listado de todos los contactos")
    for nombre in contactos:
        print(nombre,contactos[nombre])

# bloque principal

contactos=cargar()
modificar_telefono(contactos)
imprimir(contactos)