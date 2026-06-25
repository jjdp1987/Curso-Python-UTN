# Ventas mensuales (línea)
# Objetivo: visualizar tendencia y estacionalidad, anotando máximos y mínimos.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
datos = {
    "mes": ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep",
"Oct", "Nov", "Dic"],
    "ventas": [120, 150, 130, 180, 210, 190, 175, 220, 205, 230, 240, 260]
}
df = pd.DataFrame(datos).set_index("mes")
fig, ax = plt.subplots(figsize=(8, 4), layout="constrained")
(line,) = ax.plot(df.index, df["ventas"], marker="o")
ax.set_title("Ventas mensuales")
ax.set_xlabel("Mes")
ax.set_ylabel("Unidades")
i_max = df["ventas"].idxmax()
v_max = df.loc[i_max, "ventas"]
i_min = df["ventas"].idxmin()
v_min = df.loc[i_min, "ventas"]
ax.annotate(f"Máx: {v_max}", xy=(i_max, v_max), xytext=(i_max, v_max + 10),
            arrowprops={"arrowstyle": "->"})
ax.annotate(f"Mín: {v_min}", xy=(i_min, v_min), xytext=(i_min, v_min - 30),
            arrowprops={"arrowstyle": "->"})
plt.show()