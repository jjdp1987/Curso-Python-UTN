# Confeccionar un programa que genere un número aleatorio entre 1 y 100 y no se muestre.
# El operador debe tratar de adivinar el número ingresado.
# Cada vez que ingrese un número mostrar un mensaje "Gano" si es igual al generado o 
# "El número aleatorio es mayor" o "El número aleatorio es menor".
# Mostrar cuando gana el jugador cuantos intentos necesitó.

import random
intentos=0
aleatorio=random.randint(1,100)
elegido=-1
print("Intenta adivinar el numero que pense entre 1 y 100")
while (elegido!=aleatorio):
    elegido=int(input("Cual numero elige?"))
    if aleatorio>elegido:
        print("Pense un valor mayor")
    else:
        if aleatorio<elegido:
            print("Pense un valor menor")
            intentos=intentos+1
print("Ganaste en",intentos,"intentos")