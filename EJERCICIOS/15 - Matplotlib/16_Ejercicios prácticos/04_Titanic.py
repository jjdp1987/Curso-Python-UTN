# Titanic
# Objetivo: analizar tasas de supervivencia y distribuciones de edad.
# Enunciado: usá seaborn.load_dataset("titanic") para obtener el dataset (filtrá filas
# sin survived, pclass, sex o age), calculá la tasa de supervivencia por clase y sexo,
# representála con barras y construí un histograma superpuesto de edades diferenciando por
# supervivencia.

import matplotlib.pyplot as plt
import seaborn as sns
df = sns.load_dataset("titanic").dropna(subset=["survived", "pclass", "sex",
"age"])
tasas = df.groupby(["pclass", "sex"])["survived"].mean().unstack()
fig, ax = plt.subplots(layout="constrained")
tasas.plot(kind="bar", ax=ax)
ax.set_title("Tasa de supervivencia por clase y sexo")
ax.set_xlabel("Clase")
ax.set_ylabel("Tasa de supervivencia")
plt.show()
fig, ax = plt.subplots(layout="constrained")
for survived, d in df.groupby("survived"):
    ax.hist(d["age"], bins=30, density=True, alpha=0.5,
label=f"Survived={survived}")
ax.set_title("Distribución de edades por supervivencia")
ax.set_xlabel("Edad")
ax.set_ylabel("Densidad")
ax.legend(title="Survived")
plt.show()