import matplotlib.pyplot as plt
import numpy as np
print(plt.style.available) # Lista de estilos disponibles
plt.style.use("seaborn-v0_8") # Aplica estilo global hasta cambiarlo
x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)
fig, ax = plt.subplots(layout="constrained")
ax.plot(x, y, label="sin(x)")
ax.set_title("Ejemplo con estilo 'seaborn-v0_8'")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
plt.show()


#Cambiar estilo temporalmente
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)
with plt.style.context(["dark_background"]):
    fig, ax = plt.subplots(layout="constrained")
    ax.plot(x, y)
    ax.set_title("Solo este gráfico en dark_background")
    plt.show()