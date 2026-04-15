# Realizar un programa que pida cargar una fecha cualquiera, luego verificar si dicha fecha corresponde a Navidad. 

dia = int(input("Ingrese el nro de día: "))
mes = int(input("Ingrese el nro de mes: "))

if dia == 24 and mes == 12:
    print("Es navidad")