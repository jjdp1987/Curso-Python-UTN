# El gráfico de líneas es ideal para seguir la evolución de una variable en el tiempo o
# frente a otra magnitud.
import matplotlib.pyplot as plt
# Datos
meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun"]
ventas = [100, 120, 90, 140, 180, 160]
# Gráfico de líneas
plt.plot(meses, ventas, marker="o", color="blue", linestyle="-")
plt.title("Ventas mensuales")
plt.xlabel("Meses")
plt.ylabel("Ventas (en miles)")
plt.show()