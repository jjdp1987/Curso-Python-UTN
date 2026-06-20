# Casos típicos: columnas de texto a datetime64[ns], detección automática o manual de
# formatos, manejo de valores inválidos (errors="coerce") y zonas horarias (tz_localize,
# tz_convert).
import pandas as pd
df = pd.DataFrame({
    "fecha": ["2025-01-01", "2025-01-02", "01/03/2025", "2025/01/04", "2025-13-
01"],
    "valor": [10, 12, 11, 15, 14]
})
df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce", dayfirst=False)
# df["fecha"] = pd.to_datetime(df["fecha"], format="%Y-%m-%d") # Formato
explícito
df = df.set_index("fecha").sort_index()
# df = df.tz_localize("UTC").tz_convert("America/Argentina/Cordoba")
# 💡 Tips: unificá la zona horaria, ordená con df.sort_index() y documentá la política de datos
# faltantes.