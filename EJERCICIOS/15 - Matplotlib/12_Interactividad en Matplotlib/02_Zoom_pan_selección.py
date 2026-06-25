# Selección horizontal con SpanSelector

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import SpanSelector
x = np.linspace(0, 10, 500)
y = np.sin(2 * np.pi * x) * np.exp(-0.2 * x)
fig, (ax, ax_zoom) = plt.subplots(2, 1, figsize=(8, 6), layout="constrained")
ax.plot(x, y)
ax.set_title("Arrastrá para seleccionar un rango (horizontal)")
ax_zoom.set_title("Zoom del rango seleccionado")
def onselect(xmin, xmax):
    mask = (x >= xmin) & (x <= xmax)
    ax_zoom.clear()
    ax_zoom.plot(x[mask], y[mask])
    ax_zoom.set_title(f"Rango seleccionado: {xmin:.2f} a {xmax:.2f}")
    fig.canvas.draw_idle()
span = SpanSelector(
    ax,
    onselect,
    direction="horizontal",
    useblit=True,
    props=dict(alpha=0.3),
    interactive=True
)
plt.show()


# Selección rectangular con RectangleSelector

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector
rng = np.random.default_rng(0)
x = rng.normal(0, 1, 800)
y = rng.normal(0, 1, 800)
fig, ax = plt.subplots(layout="constrained")
pts = ax.scatter(x, y, s=12, alpha=0.7)
ax.set_title("Arrastrá un rectángulo para seleccionar puntos")
def onselect_rect(eclick, erelease):
    """Handle rectangular selection events from RectangleSelector.

    eclick and erelease are the press and release mouse events; use their
    xdata/ydata to compute the selected box and update the scatter alphas.
    """
    xmin, xmax = sorted([eclick.xdata, erelease.xdata])
    ymin, ymax = sorted([eclick.ydata, erelease.ydata])
    sel = (x >= xmin) & (x <= xmax) & (y >= ymin) & (y <= ymax)
    pts.set_alpha(np.where(sel, 1.0, 0.3))
    fig.canvas.draw_idle()
rect = RectangleSelector(
    ax,
    onselect_rect,
useblit=True,
button=[1],
props=dict(facecolor="tab:blue", alpha=0.15, edgecolor="k")
)
plt.show()


# RangeSlider para definir intervalos

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RangeSlider
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x) + 0.2 * np.sin(10 * x)
fig, ax = plt.subplots(figsize=(8, 5), layout="constrained")
(line,) = ax.plot(x, y)
ax.set_ylim(-2, 2)
ax_r = fig.add_axes([0.15, 0.05, 0.7, 0.04])
rs = RangeSlider(
    ax=ax_r,
    label="Rango X",
    valmin=float(x.min()),
    valmax=float(x.max()),
    valinit=(float(x.min()), float(x.max()))
)
def actualizar_rango(val):
    xmin, xmax = rs.val
    ax.set_xlim(xmin, xmax)
    fig.canvas.draw_idle()

rs.on_changed(actualizar_rango)
plt.show()


# Botón para resetear o lanzar acciones

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
x = np.linspace(0, 2 * np.pi, 400)
fig, ax = plt.subplots(figsize=(8, 5), layout="constrained")
(line,) = ax.plot(x, np.sin(1 * x))
ax.set_ylim(-1.5, 1.5)
ax_s = fig.add_axes([0.15, 0.05, 0.6, 0.04])
sl = Slider(ax=ax_s, label="Frecuencia", valmin=0.5, valmax=5.0, valinit=1.0)
def on_change(val):
    line.set_ydata(np.sin(sl.val * x))
    fig.canvas.draw_idle()
sl.on_changed(on_change)
ax_b = fig.add_axes([0.78, 0.05, 0.12, 0.04])
btn = Button(ax=ax_b, label="Reset")
def on_reset(event):
    sl.reset()
btn.on_clicked(on_reset)
plt.show()