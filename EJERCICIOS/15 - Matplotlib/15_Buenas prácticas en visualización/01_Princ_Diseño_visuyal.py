# • Claridad primero: un mensaje por gráfico; si hay varias ideas, separalas en subplots.
# • Contexto explícito: títulos informativos, ejes con unidades y fuente de datos cuando
# corresponda.
# • Orden lógico: ordená categorías por valor, alfabéticamente o cronológicamente.
# • Jerarquía tipográfica: títulos > etiquetas > ticks > leyenda; evitá textos inclinados.
# • Color con intención: paleta corta, apta para daltónicos; usá grosor o intensidad para
# enfatizar.
# • Data-ink ratio: eliminá adornos, bordes dobles y grillas fuertes; mantené una grilla suave
# (alpha bajo).
# • Consistencia visual: misma tipografía, paleta y grosores en todo el informe.


import matplotlib as mpl
from cycler import cycler
mpl.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "axes.titlesize": 12,
    "axes.labelsize": 10,
    "axes.grid": True,
    "grid.linestyle": "--",
    "grid.alpha": 0.35,
    "lines.linewidth": 1.6,
    "lines.markersize": 4.0,
    "legend.frameon": False,
})
mpl.rcParams["axes.prop_cycle"] = cycler(color=[
    "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728",
    "#9467bd", "#8c564b", "#e377c2", "#7f7f7f"
])