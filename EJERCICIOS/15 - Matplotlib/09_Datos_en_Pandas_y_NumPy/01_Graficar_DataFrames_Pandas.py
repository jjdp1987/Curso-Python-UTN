# Line plot y bar plot desde un DataFrame
import matplotlib.pyplot as plt
import pandas as pd
# Datos de ejemplo
df = pd.DataFrame({
"mes": ["Ene", "Feb", "Mar", "Abr", "May", "Jun"],
"ventas": [120, 150, 90, 180, 220, 210],
"costos": [80, 95, 70, 120, 140, 150],
}).set_index("mes")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4), layout="constrained")
df.plot(ax=ax1, marker="o")
ax1.set_title("Ventas vs. Costos (líneas)")
ax1.set_xlabel("Mes")
ax1.set_ylabel("Monto")
df["ventas"].plot(kind="bar", ax=ax2)
ax2.set_title("Ventas (barras)")
ax2.set_xlabel("Mes")
ax2.set_ylabel("Monto")
plt.show()

# Gráficos por grupo (groupby) y subplots
import matplotlib.pyplot as plt
import pandas as pd
datos = [
{"categoria": "A", "mes": "Ene", "valor": 10},
{"categoria": "A", "mes": "Feb", "valor": 16},
{"categoria": "B", "mes": "Ene", "valor": 7},
{"categoria": "B", "mes": "Feb", "valor": 9},
]
df = pd.DataFrame(datos)
pivot = df.pivot(index="mes", columns="categoria", values="valor")
fig, ax = plt.subplots(layout="constrained")
pivot.plot(ax=ax, marker="o")
ax.set_title("Pivot + plot")
ax.set_xlabel("Mes")
ax.set_ylabel("Valor")
plt.show()

# Series temporales con DatetimeIndex
import matplotlib.pyplot as plt
import pandas as pd
rng = pd.date_range("2025-01-01", periods=60, freq="D")
serie = pd.Series(range(60), index=rng).rolling(7).mean()
fig, ax = plt.subplots(figsize=(8, 4), layout="constrained")
serie.plot(ax=ax)
ax.set_title("Serie temporal con media móvil (7D)")
ax.set_xlabel("Fecha")
ax.set_ylabel("Valor")
plt.show()