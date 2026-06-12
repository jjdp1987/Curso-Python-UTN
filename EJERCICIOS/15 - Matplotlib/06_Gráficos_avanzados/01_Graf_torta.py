# Los gráficos de torta muestran proporciones de un total. Funcionan mejor con pocas categorías y
# diferencias bien marcadas.
# Puntos clave
# • Utilizá Axes.pie para crear el gráfico desde un objeto Axes.
# • Mantené la relación de aspecto en 1:1 con ax.set_aspect('equal') para obtener un
# círculo.
# • autopct muestra porcentajes formateados.
# • explode resalta sectores relevantes.
# • labels o ax.legend() facilitan la lectura.

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
valores = [40, 25, 20, 15]
labels = ["Ventas", "Marketing", "I+D", "Operaciones"]
explode = [0.05, 0, 0, 0] # Resaltar "Ventas"
ax.pie(
valores,
labels=labels,
explode=explode,
autopct="%.1f%%",
startangle=90,
wedgeprops={"linewidth": 1, "edgecolor": "white"}
)
ax.set_title("Distribución de presupuesto")
ax.set_aspect('equal') # Círculo perfecto
plt.show()