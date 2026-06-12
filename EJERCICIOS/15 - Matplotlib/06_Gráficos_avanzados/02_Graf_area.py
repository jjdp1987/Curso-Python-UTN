# Estos gráficos destacan el área bajo una curva o entre dos curvas, útiles para bandas de confianza,
# rangos o acumulados.
# Área bajo una curva

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 200)
y = np.sin(x) + 1.5

fig, ax = plt.subplots()
ax.plot(x, y, label="Señal")
ax.fill_between(x, y, 0, alpha=0.3) # Relleno hasta el eje X
ax.set_title("Área bajo la curva")
ax.set_xlabel("Tiempo")
ax.set_ylabel("Amplitud")
ax.legend()
plt.show()


# Área entre dos curvas
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2 * np.pi, 300)
y1 = np.sin(x) + 1
y2 = np.cos(x) + 1
fig, ax = plt.subplots()
ax.plot(x, y1, label="Seno")
ax.plot(x, y2, label="Coseno")
ax.fill_between(x, y1, y2, where=(y1 >= y2), alpha=0.25, label="Área (y1 >=y2)")
ax.fill_between(x, y1, y2, where=(y1 < y2), alpha=0.25, label="Área (y1 < y2)")
ax.set_title("Área entre dos curvas")
ax.set_xlabel("Ángulo")
ax.set_ylabel("Valor")
ax.legend()
plt.show()