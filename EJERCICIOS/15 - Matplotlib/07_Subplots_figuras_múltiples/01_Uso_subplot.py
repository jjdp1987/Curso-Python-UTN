import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2 * np.pi, 200)
# Sintaxis moderna: Figure y arreglo de Axes
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(8, 6), layout='constrained')
# 'layout="constrained"' ayuda a evitar solapamientos de textos y etiquetas.
axs[0, 0].plot(x, np.sin(x))
axs[0, 0].set_title("sin(x)")
axs[0, 1].plot(x, np.cos(x), linestyle="--")
axs[0, 1].set_title("cos(x)")
axs[1, 0].plot(x, np.tan(x))
axs[1, 0].set_title("tan(x)")
axs[1, 0].set_ylim(-3, 3) # Acotar tan(x)
axs[1, 1].plot(x, np.sin(x) * np.cos(x), marker="o", markersize=2,
linestyle="-")
axs[1, 1].set_title("sin(x)*cos(x)")
fig.suptitle("Cuadrícula 2x2 con subplots", fontsize=12)
plt.show()