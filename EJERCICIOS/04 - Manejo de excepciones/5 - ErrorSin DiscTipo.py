#Realizar la carga de dos números por teclado e imprimir la división del primero respecto al
#segundo. Capturar cualquier tipo de excepción que se dispare.

try:
    valor1=int(input("Ingrese dividendo:"))
    valor2=int(input("Ingrese divisor:"))
    division=valor1/valor2
    print("El resultado de la división es", division)
except:
    print("Problemas con la entrada u operación")

# Como podemos ver no disponemos un nombre de excepción después de la palabra clave 'except':
# except:
#     print("Problemas con la entrada u operación")