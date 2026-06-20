# Ajustes globales con rcParams

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams.update({
"font.family": "DejaVu Sans",
"font.size": 11,
"figure.facecolor": "#FFFFFF",
"axes.facecolor": "#FAFAFA",
"axes.edgecolor": "#333333",
"axes.grid": True,
"grid.linestyle": "--",
"grid.alpha": 0.4,
"axes.titlesize": 13,
"axes.labelsize": 11,
"legend.frameon": False,
})
x = np.linspace(0, 10, 200)
y = np.exp(-0.2 * x) * np.sin(3 * x)
fig, ax = plt.subplots(layout="constrained")
ax.plot(x, y, marker="o", markersize=3)
ax.set_title("Fuente, grilla y fondos personalizados (global)")
ax.set_xlabel("Tiempo")
ax.set_ylabel("Amplitud")
plt.show()

#Ajustes locales por figura
import matplotlib.pyplot as plt
fig, ax = plt.subplots(layout="constrained")
ax.set_facecolor("#f0f7ff")
fig.set_facecolor("#ffffff")
ax.grid(True, linestyle=":", alpha=0.5)
ax.set_title("Ajustes locales")
plt.show()

#Ciclo de colores moderno (cycler)
import matplotlib as mpl
from cycler import cycler
mpl.rcParams["axes.prop_cycle"] = cycler(color=[
"#1f77b4", "#ff7f0e", "#2ca02c", "#d62728",
"#9467bd", "#8c564b", "#e377c2", "#7f7f7f"
])
#Definir un ciclo garantiza que cada serie reciba 📈 colores armónicos y reproducibles.