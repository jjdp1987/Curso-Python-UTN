# Se cargan por teclado tres números distintos. Mostrar por pantalla el mayor de ellos. 

x1 = int(input("Ingresar el primer numero"))
x2 = int(input("Ingresar el segundo numero"))
x3 = int(input("Ingresar el tercer numero"))

if x1 > x2 and x1 > x3:
    print(f"El número {x1} es el mayor")
elif x2 > x3:
    print(f"El número {x2} es el mayor")
else:
    print(f"El número {x3} es el mayor")