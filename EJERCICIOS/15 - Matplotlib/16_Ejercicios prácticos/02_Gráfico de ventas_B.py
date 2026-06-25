# Ventas por categoría (barras)
# Objetivo: comparar categorías, ordenando y etiquetando valores.

import matplotlib.pyplot as plt
import pandas as pd
df = pd.DataFrame({
    "categoria": ["A", "B", "C", "D", "E", "F"],
    "unidades": [420, 280, 560, 310, 150, 480]
}).sort_values("unidades")
fig, ax = plt.subplots(figsize=(7, 4), layout="constrained")
ax.barh(df["categoria"], df["unidades"])
ax.set_title("Unidades vendidas por categoría")
ax.set_xlabel("Unidades")
for y, v in zip(df["categoria"], df["unidades"]):
    ax.text(v, y, f"{v}", va="center", ha="left")
plt.show()