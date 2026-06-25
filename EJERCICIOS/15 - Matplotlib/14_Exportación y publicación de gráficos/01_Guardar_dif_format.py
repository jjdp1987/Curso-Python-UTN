import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x)
fig, ax = plt.subplots(figsize=(6, 4), layout="constrained")
ax.plot(x, y, label="sin(x)")
ax.set_title("Ejemplo de exportación")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
fig.savefig("grafico.png", dpi=200, bbox_inches="tight")
fig.savefig("grafico.pdf", bbox_inches="tight")
fig.savefig("grafico.svg", bbox_inches="tight")