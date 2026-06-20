import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
muestras = np.random.normal(loc=0, scale=1, size=2000)
fig, ax = plt.subplots()

# Histograma como densidad
ax.hist(
muestras,
bins="auto",
density=True,
edgecolor="black",
alpha=0.4,
label="Hist (densidad)"
)

# Curva normal estimada con media y desvío de los datos
mu, sigma = np.mean(muestras), np.std(muestras, ddof=1)
x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 400)
pdf = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) **
2)

ax.plot(x, pdf, linewidth=2, label=f"N(mu={mu:.2f}, sigma={sigma:.2f})")
ax.set_title("Distribución y densidad (hist con density=True)")
ax.set_xlabel("Valor")
ax.set_ylabel("Densidad")
ax.legend()
plt.show()