# • Ejes truncados sin aviso: mostrá el rango completo o anotá claramente el truncado.
# • Escalas inadecuadas: usá logaritmos para crecimientos multiplicativos e indicá la escala.
# • Demasiadas series: desglosá en subplots o facetado; etiquetá líneas directamente.
# • Exceso de colores: preferí paleta corta y consistente; verificá contraste.
# • 3D innecesario: solo si la tercera dimensión aporta información real.
# • Pie charts con demasiados segmentos: sustituí por barras o barras apiladas.
# • Doble eje Y confuso: optá por subplots con sharex o normalizá las series.
# • Binning inconsistente en histogramas: mismo número de bins y rango al comparar grupos.
# • Ticks ilegibles: reducí cantidad, rotá en 45° o abreviá etiquetas.
# • No mostrar incertidumbre: agrega bandas, barras de error o anotaciones.
import numpy as np
import matplotlib.pyplot as plt
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3), layout="constrained")
ax1.bar(["A", "B"], [100, 105])
ax1.set_title("Eje completo")
ax2.bar(["A", "B"], [100, 105])
ax2.set_ylim(95, 106)
ax2.set_title("Eje truncado (aclarar!)")
plt.show()