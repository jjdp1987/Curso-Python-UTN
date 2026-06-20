#Tema como diccionario en código

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from cycler import cycler
mi_tema = {
    "font.family": "DejaVu Sans",
    "font.size": 11,
    "figure.facecolor": "#ffffff",
    "axes.facecolor": "#fbfbfb",
    "axes.edgecolor": "#222222",
    "axes.titlesize": 14,
    "axes.labelsize": 11,
    "axes.grid": True,
    "grid.color": "#aaaaaa",
    "grid.linestyle": "--",
    "grid.linewidth": 0.6,
    "grid.alpha": 0.5,
    "legend.frameon": False,
    "axes.prop_cycle": cycler(color=["#2D81FF", "#FF6B6B", "#2ECC71",
    "#F1C40F", "#9B59B6"]),
    "lines.linewidth": 2.0,
    "lines.markersize": 4.0,
}
x = np.linspace(0, 2 * np.pi, 300)
with mpl.rc_context(mi_tema):
    fig, ax = plt.subplots(layout="constrained")
    ax.plot(x, np.sin(x), marker="o", label="sin")
    ax.plot(x, np.cos(x), marker="s", label="cos")
    ax.set_title("Tema personalizado (contexto)")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    plt.show()
# Para aplicarlo de forma global:
# mpl.rcParams.update(mi_tema)



#Tema en archivo .mplstyle
# mi_tema.mplstyle
# font.family: DejaVu Sans
# font.size: 11
# figure.facecolor: #ffffff
# axes.facecolor: #fbfbfb
# axes.edgecolor: #222222
# axes.titlesize: 14
# axes.labelsize: 11
# axes.grid: True
# grid.color: #aaaaaa
# grid.linestyle: --
# grid.linewidth: 0.6
# grid.alpha: 0.5
# legend.frameon: False
# lines.linewidth: 2.0
# lines.markersize: 4.0
# axes.prop_cycle: color: #2D81FF, #FF6B6B, #2ECC71, #F1C40F, #9B59B6

# Guardá el archivo en una carpeta reconocida por Matplotlib (por ejemplo, ~/.config/matplotlib/stylelib/ en Linux/macOS o C:\Usuarios\
# TU_USUARIO\.matplotlib\stylelib\ en Windows).

import matplotlib.pyplot as plt
import numpy as np
plt.style.use("mi_tema") # Si está en stylelib
# plt.style.use("./mi_tema.mplstyle") # Ruta relativa
x = np.linspace(0, 1, 100)
fig, ax = plt.subplots(layout="constrained")
ax.plot(x, x**2, label="x^2")
ax.plot(x, x**3, label="x^3")
ax.set_title("Usando mi_tema.mplstyle")
ax.legend()
plt.show()