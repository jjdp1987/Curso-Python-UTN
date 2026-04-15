# Realizar la carga de dos números por teclado e imprimir la división del primero respecto al
# segundo, capturar las excepciones ZeroDivisionError y ValueError.

try:
    valor1=int(input("Ingrese dividendo:"))
    valor2=int(input("Ingrese divisor:"))
    division=valor1/valor2
    print("El resultado de la división es", division)
except ZeroDivisionError:
    print("No se puede dividir por cero.")
except ValueError:
    print("Los valores a ingresar deben ser enteros")

# Debemos disponer los dos bloques 'except' a la misma altura indicando el nombre de la excepción a capturar:
#except ZeroDivisionError:
#    print("No se puede dividir por cero.")
#except ValueError:
#    print("Los valores a ingresar deben ser enteros")
