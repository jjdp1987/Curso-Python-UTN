#ejemplo 1

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
x = np.linspace(0, 2 * np.pi, 300)
fig = plt.figure(figsize=(9, 6), layout='constrained')
gs = GridSpec(nrows=2, ncols=2, figure=fig, height_ratios=[2, 1])
ax_top = fig.add_subplot(gs[0, :])
ax_top.plot(x, np.sin(x), label="sin(x)")
ax_top.plot(x, np.cos(x), label="cos(x)")
ax_top.set_title("Superior: sin y cos")
ax_top.legend()
ax_bl = fig.add_subplot(gs[1, 0])
ax_bl.plot(x, np.sin(2 * x), color="purple")
ax_bl.set_title("Inferior Izq: sin(2x)")
ax_br = fig.add_subplot(gs[1, 1])
ax_br.plot(x, np.cos(2 * x), color="green")
ax_br.set_title("Inferior Der: cos(2x)")
fig.suptitle("Diseño avanzado con GridSpec (1 grande arriba, 2 abajo)")
plt.show()

#ejemplo 2

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
t = np.linspace(0, 6 * np.pi, 600)
fig = plt.figure(figsize=(10, 6), layout='constrained')
gs = GridSpec(
nrows=2,
ncols=3,
figure=fig,
width_ratios=[1, 2, 2],
height_ratios=[1, 1]
)
ax_left = fig.add_subplot(gs[:, 0])
ax_left.plot(t, np.sin(t), linewidth=1)
ax_left.set_title("Panel izquierdo (2 filas)")
ax_c_top = fig.add_subplot(gs[0, 1])
ax_c_top.plot(t, np.cos(t), color="orange")
ax_c_top.set_title("Centro arriba")
ax_c_bot = fig.add_subplot(gs[1, 1])
ax_c_bot.plot(t, np.sin(2 * t), color="green")
ax_c_bot.set_title("Centro abajo")
ax_right = fig.add_subplot(gs[:, 2])
ax_right.plot(t, np.cos(2 * t), color="red")
ax_right.set_title("Derecha (2 filas)")
fig.suptitle("GridSpec con anchos asimétricos y spans de filas")
plt.show()

#ejemplo 3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
x = np.linspace(0, 10, 400)
fig = plt.figure(figsize=(9, 6), layout='constrained')
gs = GridSpec(2, 2, figure=fig)
ax_main = fig.add_subplot(gs[:, 0])
ax_tr = fig.add_subplot(gs[0, 1], sharex=ax_main)
ax_br = fig.add_subplot(gs[1, 1], sharex=ax_main)
ax_main.plot(x, np.sin(x), label="sin(x)")
ax_main.set_title("Principal")
ax_main.legend()
ax_tr.plot(x, np.sin(2 * x), color="purple")
ax_tr.set_title("Arriba derecha (sharex)")
ax_br.plot(x, np.sin(3 * x), color="orange")
ax_br.set_title("Abajo derecha (sharex)")
ax_br.set_xlabel("Tiempo")
plt.setp(ax_tr.get_xticklabels(), visible=False)
fig.suptitle("GridSpec + sharex entre subplots")
plt.show()