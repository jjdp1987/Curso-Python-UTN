# Resampleo a semanal/mensual
semana = df["valor"].resample("W").mean()
mes = df["valor"].resample("M").sum()


# Ventanas móviles (rolling)
media7 = df["valor"].rolling(window=7, center=True, min_periods=1).mean()
mediana7 = df["valor"].rolling(7, center=True, min_periods=1).median()


# Suavizado exponencial (EWM)
ewm14 = df["valor"].ewm(span=14, adjust=False).mean()


# Tendencia integradora
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(9, 4), layout="constrained")
ax.plot(df.index, df["valor"], alpha=0.4, label="Diario")
ax.plot(semana.index, semana, linewidth=2, label="Semanal (mean)")
ax.plot(media7.index, media7, linewidth=2, label="Media móvil 7D")
ax.plot(ewm14.index, ewm14, linewidth=2, label="EWM 14")
ax.set_title("Resampleo y tendencias")
ax.set_xlabel("Fecha")
ax.set_ylabel("Valor")
ax.legend()
plt.show()


# Resampleo mensual y suavizado
mensual_mean = df["valor"].resample("M").mean()
mensual_mean_3 = mensual_mean.rolling(3, min_periods=1).mean()
fig, ax = plt.subplots(figsize=(8, 4), layout="constrained")
ax.plot(mensual_mean.index, mensual_mean, marker="o", label="Mensual (mean)")
ax.plot(mensual_mean_3.index, mensual_mean_3, label="Mensual suavizada (3M)")
ax.set_title("Promedio mensual y suavizado 3 meses")
ax.set_ylabel("Valor")
ax.legend()
plt.show()