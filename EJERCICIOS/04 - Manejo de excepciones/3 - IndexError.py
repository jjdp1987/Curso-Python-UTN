# Almacenar en una tupla los nombres de meses del año. Solicitar el ingreso del número de mes y
# mostrar seguidamente el nombre de dicho mes. Capturar la excepción IndexError

meses = ("enero","febrero","marzo","abril","mayo","junio",
 "julio","agosto","septiembre","octubre","noviembre","diciembre")
try:
    nromes=int(input("Ingrese un número de mes [1-12]:"))
    print(meses[nromes-1])
except IndexError:
    print("En número de mes debe ir entre 1 y 12")

# Con este algoritmo si el operador ingresa un valor superior a 12 luego se captura la excepción
# IndexError. Pero tenemos el problema si carga un valor 0 o inferior a 0 luego las tuplas pueden
# disponer valores negativos, por lo que estos casos lo podemos resolver con un if:

meses=("enero","febrero","marzo","abril","mayo","junio",
 "julio","agosto","septiembre","octubre","noviembre","diciembre")

try:
    nromes=int(input("Ingrese un número de mes [1-12]:"))
    if nromes>0:
        print(meses[nromes-1])
    else:
        print("En número de mes debe ir entre 1 y 12")
except IndexError:
    print("En número de mes debe ir entre 1 y 12")
