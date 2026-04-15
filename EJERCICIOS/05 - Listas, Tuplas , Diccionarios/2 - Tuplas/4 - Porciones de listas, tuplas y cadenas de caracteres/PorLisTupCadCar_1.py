# Confeccionar una función que le enviemos un número de mes como parámetro y nos retorne una
# tupla con todos los nombres de meses que faltan hasta fin de año.

def meses_faltantes(numeromes):
    meses=('enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre')
    return meses[numeromes:]

# bloque principal

print("Imprimir los nombres de meses que faltan hasta fin de año")
numeromes=int(input("Ingrese el numero de mes:"))
mesesfalta=meses_faltantes(numeromes)
print(mesesfalta)