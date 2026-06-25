# Ventas vs. Presupuesto (barras agrupadas)
# Objetivo: comparar dos métricas por categoría y resaltar diferencias.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df = pd.DataFrame({
    "categoria": ["A", "B", "C", "D"],
    "ventas": [120, 95, 180, 140],
    "presupuesto": [100, 110, 160, 150]
})
x = np.arange(len(df))
width = 0.38
fig, ax = plt.subplots(figsize=(7, 4), layout="constrained")
ax.bar(x - width / 2, df["ventas"], width=width, label="Ventas")
ax.bar(
    x + width / 2,
    df["presupuesto"],
    width=width,
    label="Presupuesto",
    color=["#2ca02c" if v <= p else "#d62728" for v, p in zip(df["ventas"],
df["presupuesto"])]
)
ax.set_xticks(x, df["categoria"])
ax.set_title("Ventas vs Presupuesto")
ax.set_ylabel("Monto")
ax.legend()
plt.show()