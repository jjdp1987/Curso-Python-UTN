# En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar 
# un programa que lea los sueldos que cobra cada empleado e informe cuántos empleados cobran 
# entre $100 y $300 y cuántos cobran más de $300. Además el programa deberá informar el importe 
# que gasta la empresa en sueldos al personal.

n = int(input("Ingrese el nro de empleados: "))
x = 1
sueld_1 = 0
sueld_2 = 0
acum_1 = 0
acum_2 = 0

while x <= n:
    sueldo = int(input("Ingresar sueldo del empleado: "))
        
    if sueldo >= 100 and sueldo < 300:
        acum_1 += 1
        sueld_1 += sueldo
    else:
        acum_2 += 1
        sueld_2 += sueldo
    
    x += 1

gasto = sueld_1 + sueld_2
print(f"Los empleados que ganan entre 100 y 300 pesos son {acum_1}")
print(f"Los empleados que ganan mas de 300 pesos son {acum_2}")
print(f"La empresa gasta en sueldos {gasto} pesos")