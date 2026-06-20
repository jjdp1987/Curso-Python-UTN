# Graficar arrays NumPy en Axes
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 2 * np.pi, 300)
y1 = np.sin(x)
y2 = np.cos(x)
fig, ax = plt.subplots(layout="constrained")
ax.plot(x, y1, label="sin(x)")
ax.plot(x, y2, label="cos(x)")
ax.set_title("Arrays NumPy + Matplotlib")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
plt.show()

# Calcular con NumPy y almacenar en Pandas
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
x = np.linspace(0, 10, 200)
signal = np.exp(-0.2 * x) * np.sin(3 * x)
df = pd.DataFrame({"x": x, "signal": signal})
df["suavizada"] = pd.Series(signal).rolling(5, center=True).mean()
fig, ax = plt.subplots(layout="constrained")
ax.plot(df["x"], df["signal"], label="Señal")
ax.plot(df["x"], df["suavizada"], label="Suavizada (rolling 5)")
ax.set_title("Mezcla Pandas + NumPy")
ax.set_xlabel("x")
ax.set_ylabel("Amplitud")
ax.legend()
plt.show()

# De DataFrame a NumPy para vectorizar
import numpy as np
v = df["signal"].to_numpy()
df["abs_signal"] = np.abs(v)