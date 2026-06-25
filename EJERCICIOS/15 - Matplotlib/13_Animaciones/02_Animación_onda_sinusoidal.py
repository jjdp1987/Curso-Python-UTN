# Onda viajera (una línea)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
x = np.linspace(0, 2 * np.pi, 600)
fig, ax = plt.subplots(figsize=(7, 4), layout="constrained")
(line,) = ax.plot(x, np.sin(x))
ax.set_xlim(x.min(), x.max())
ax.set_ylim(-1.2, 1.2)
ax.set_title("Onda sinusoidal animada")
ax.set_xlabel("x")
ax.set_ylabel("y = sin(x - fase)")
def init():
    line.set_ydata(np.sin(x))
    return (line,)
def update(frame):
    fase = 0.05 * frame
    line.set_ydata(np.sin(x - fase))
    return (line,)
ani = FuncAnimation(
    fig,
    update,
    frames=200,
    init_func=init,
    interval=20,
    blit=True,
    repeat=True
)
plt.show()


# Dos líneas y anotación

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
x = np.linspace(0, 2 * np.pi, 600)
fig, ax = plt.subplots(figsize=(7, 4), layout="constrained")
line1, = ax.plot(x, np.sin(x))
line2, = ax.plot(x, np.cos(x))
txt = ax.text(0.02, 0.90, "", transform=ax.transAxes)
ax.set_ylim(-1.2, 1.2)
ax.set_title("sin/cos animados")
def init():
    line1.set_ydata(np.sin(x))
    line2.set_ydata(np.cos(x))
    txt.set_text("")
    return (line1, line2, txt)
def update(i):
    fase = 0.04 * i
    line1.set_ydata(np.sin(x - fase))
    line2.set_ydata(np.cos(x - fase))
    txt.set_text(f"frame: {i}")
    return (line1, line2, txt)
ani = FuncAnimation(
    fig,
    update,
    frames=250,
    init_func=init,
    interval=20,
    blit=True
)
plt.show()

