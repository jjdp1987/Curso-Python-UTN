# Realizar la carga de dos números por teclado e imprimir la división del primero respecto al
# segundo, capturar la excepción ZeroDivisionError.

try:
    valor1=int(input("Ingrese dividendo:"))
    valor2=int(input("Ingrese divisor:"))
    division=valor1/valor2
    print("El resultado de la división es", division)
except ZeroDivisionError:
    print("No se puede dividir por cero.")
