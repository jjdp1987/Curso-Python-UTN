import matplotlib.pyplot as plt
# Datos de ejemplo
grupo1 = [7, 8, 5, 6, 9, 10, 6, 7, 8, 6]
grupo2 = [5, 6, 7, 8, 7, 9, 5, 6, 6, 7]
plt.boxplot([grupo1, grupo2], tick_labels=["Grupo 1", "Grupo 2"])
plt.title("Comparación de dos grupos")
plt.ylabel("Valores")
plt.show()