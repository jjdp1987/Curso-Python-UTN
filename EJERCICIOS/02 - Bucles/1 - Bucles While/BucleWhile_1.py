# Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe cuántos
# tienen notas mayores o iguales a 7 y cuántos menores.

contador = 1
notas_mayores_7 = 0
notas_menores_7 = 0

while contador <= 10:
    nota = float(input("Ingrese la nota del alumno: "))
    
    if nota >= 7:
        notas_mayores_7 += 1
    else:
        notas_menores_7 += 1
    
    contador += 1    
print(f"Notas mayores o iguales a 7: {notas_mayores_7}")
print(f"Notas menores a 7: {notas_menores_7}")