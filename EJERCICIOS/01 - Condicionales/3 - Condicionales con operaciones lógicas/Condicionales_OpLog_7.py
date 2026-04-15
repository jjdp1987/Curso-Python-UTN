# Escribir un programa en el cual: dada una lista de tres valores numéricos distintos se calcule e informe
#  su rango de variación (debe mostrar el mayor y el menor de ellos).
# Solución:

# Ingreso de datos
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

# Cálculo del mayor y menor
mayor = max(num1, num2, num3)
menor = min(num1, num2, num3)
# Salida de resultados
print(f"El mayor número es: {mayor}")
print(f"El menor número es: {menor}")
