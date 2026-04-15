# Un postulante a un empleo, realiza un test de capacitación, se obtuvo la siguiente información: cantidad total 
# de preguntas que se le realizaron y la cantidad de preguntas que contestó correctamente. Se pide confeccionar un 
# programa que ingrese los dos datos por teclado e informe el nivel del mismo según el porcentaje de respuestas
# 
#  correctas que ha obtenido, y sabiendo que:
# Nivel máximo: Porcentaje >= 90%
# Nivel medio: Porcentaje >= 75% y < 90%
# Nivel regular: Porcentaje >= 50% y < 75%
# Nivel bajo: Porcentaje < 50%

total_preguntas = int(input("Ingrese el total de preguntas : "))
preguntas_correctas = int(input("Ingrese las prefuntas respondidas correctamente: "))

promedio = (preguntas_correctas / total_preguntas)

if promedio >= 0.9:
    print("Nivel máximo")
elif promedio >= 0.75 and promedio < 0.9:
    print("Nivel medio")
elif promedio >= 0.5 and promedio < 0.75:
    print("Nivel regular")
else:
    print("Nivel bajo")