import matplotlib.pyplot as plt
import pandas as pd
df = pd.DataFrame({
    "fecha": ["2025-01-01", "2025-01-02", "01/03/2025", "2025/01/04", "2025-01-13"],
    "valor": [10, 12, 11, 15, 14]
})
df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce", dayfirst=False)
# df["fecha"] = pd.to_datetime(df["fecha"], format="%Y-%m-%d") # Formato
explicito
df = df.set_index("fecha").sort_index()
# df = df.tz_localize("UTC").tz_convert("America/Argentina/Cordoba")
fig, ax = plt.subplots(figsize=(8, 4), layout="constrained")
ax.plot(df.index, df["valor"], marker="o")
ax.set_title("Serie de tiempo: valor diario")
ax.set_xlabel("Fecha")
ax.set_ylabel("Valor")
plt.show()


# Formateo de ejes de fecha
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
df = pd.DataFrame({
    "fecha": ["2025-01-01", "2025-01-02", "01/03/2025", "2025/01/04", "2025-01-13"],
    "valor": [10, 12, 11, 15, 14]
})
df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce", dayfirst=False)
# df["fecha"] = pd.to_datetime(df["fecha"], format="%Y-%m-%d") # Formato
explicito
df = df.set_index("fecha").sort_index()
# df = df.tz_localize("UTC").tz_convert("America/Argentina/Cordoba")
fig, ax = plt.subplots(figsize=(8, 4), layout="constrained")
ax.plot(df.index, df["valor"])
locator = mdates.AutoDateLocator()
formatter = mdates.ConciseDateFormatter(locator)
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
ax.set_title("Fechas con formateo conciso")
ax.set_xlabel("Fecha")
ax.set_ylabel("Valor")
plt.show()

# Múltiples series y leyenda
import matplotlib.pyplot as plt
import pandas as pd
df = pd.DataFrame({
    "fecha": ["2025-01-01", "2025-01-02", "01/03/2025", "2025/01/04", "2025-01-13"],
    "valor": [10, 12, 11, 15, 14]
})
df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce", dayfirst=False)
# df["fecha"] = pd.to_datetime(df["fecha"], format="%Y-%m-%d") # Formato
explicito
df = df.set_index("fecha").sort_index()
# df = df.tz_localize("UTC").tz_convert("America/Argentina/Cordoba")
fig, ax = plt.subplots(figsize=(8, 4), layout="constrained")
ax.plot(df.index, df["valor"], label="Valor A", marker="o")
# ax.plot(df.index, df["valor_b"], label="Valor B", linestyle="--")
ax.legend()
ax.set_title("Varias series temporales")
plt.show()