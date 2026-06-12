import matplotlib.pyplot as plt
fig, axs = plt.subplots(2, 2) # 2 filas, 2 columnas
axs[0, 0].plot([1, 2, 3], [1, 2, 3])
axs[0, 0].set_title("Arriba Izq.")
axs[0, 1].plot([1, 2, 3], [1, 4, 9])
axs[0, 1].set_title("Arriba Der.")
axs[1, 0].plot([1, 2, 3], [1, 8, 27])
axs[1, 0].set_title("Abajo Izq.")
axs[1, 1].plot([1, 2, 3], [1, 16, 81])
axs[1, 1].set_title("Abajo Der.")
plt.tight_layout() # Ajusta espacios
plt.show()