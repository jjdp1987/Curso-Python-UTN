# Se ingresan tres notas de un alumno, si el promedio es mayor o igual a siete mostrar un mensaje "Promocionado". 

n1 = int(input("Ingresar primer nota: "))
n2 = int(input("Ingresar segunda nota: "))
n3 = int(input("Ingresar tercera nota: "))

promedio = (n1 + n2 + n3) / 3

if promedio >= 7:
    print("Promocionado")