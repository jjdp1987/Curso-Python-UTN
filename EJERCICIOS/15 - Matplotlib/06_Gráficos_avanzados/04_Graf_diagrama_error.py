import numpy as np
import matplotlib.pyplot as plt
x = np.arange(1, 6)
y = np.array([2.0, 2.5, 3.7, 3.2, 4.1])
yerr = np.array([0.2, 0.3, 0.25, 0.35, 0.2]) # Error vertical
fig, ax = plt.subplots()
ax.errorbar(
x,
y,
yerr=yerr,
fmt="o-", # Marcador + línea
capsize=4, # Tapa de las barras de error
elinewidth=1.2, # Grosor de la barra de error
label="Medición con error"
)
ax.set_title("Diagrama de error (errorbar)")
ax.set_xlabel("Muestra")
ax.set_ylabel("Valor medido")
ax.legend()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0.5, 2.5, 5)
y = np.array([1.5, 1.8, 2.1, 2.0, 2.3])
xerr = 0.1
yerr = [0.05, 0.1, 0.08, 0.12, 0.06]
fig, ax = plt.subplots()
ax.errorbar(
x,
y,
xerr=xerr,
yerr=yerr,
fmt="s--",
capsize=3,
ecolor="gray",
label="Error en X e Y"
)
ax.set_title("Barras de error en ambos ejes")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.legend()
plt.show()