import numpy as np
import matplotlib.pyplot as plt
import time
plt.ion()
fig, ax = plt.subplots(layout="constrained")
x = np.linspace(0, 2 * np.pi, 300)
(line,) = ax.plot(x, np.sin(x), label="sin(x)")
ax.set_ylim(-1.5, 1.5)
ax.legend()
fig.canvas.draw_idle()
for f in np.linspace(1, 3, 30):
    y = np.sin(f * x)
    line.set_ydata(y)
    ax.set_title(f"Frecuencia: {f:.2f} Hz")
    fig.canvas.draw_idle()
    fig.canvas.flush_events()
time.sleep(0.05)
plt.ioff()
plt.show()