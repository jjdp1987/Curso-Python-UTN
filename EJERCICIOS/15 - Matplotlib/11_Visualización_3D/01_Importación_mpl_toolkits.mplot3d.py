# Desde Matplotlib moderno basta con crear el subplot con proyección 3D, sin importar Axes3D
# explícitamente.

import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots(subplot_kw={"projection": "3d"}, figsize=(7, 5),
layout="constrained")
t = np.linspace(0, 2 * np.pi, 200)
x, y, z = np.cos(t), np.sin(t), t
ax.plot3D(x, y, z)
ax.set_title("Ejemplo 3D: hélice simple")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()


