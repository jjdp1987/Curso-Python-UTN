# Crear un diccionario en Python que defina como clave el número de documento de una persona y como valor un string con su nombre.
# Desarrollar las siguientes funciones:
# 1) Cargar por teclado los datos de 4 personas.
# 2) Listado completo del diccionario.
# 3) Consulta del nombre de una persona ingresando su número de documento.

def cargar():
    personas={}
    for x in range(4):
        numero=int(input("Ingrese el numero de documento:"))
        nombre=input("Ingrese el nombre:")
        personas[numero]=nombre
    return personas

def imprimir(personas):
    print("Listado del diccionario completo")
    for numero in personas:
        print(numero, personas[numero])

def consulta_por_numero(personas):
    nro=int(input("Ingrese el numero de documento a consultar:"))
    if nro in personas:
        print("Nombre de la persona:",personas[nro])
    else:
        print("No existe una persona con dicho numero de documento")

# bloque principal

personas=cargar()
imprimir(personas)
consulta_por_numero(personas)