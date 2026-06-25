import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter
def build_animation(fps=30, frames=300, save=None):
    x = np.linspace(0, 2 * np.pi, 800)
    fig, ax = plt.subplots(figsize=(7, 4), layout="constrained")
    (line,) = ax.plot(x, np.sin(x))
    ax.set_ylim(-1.2, 1.2)
    ax.set_title("Patrón reusable")
    def init():
        line.set_ydata(np.sin(x))
        return (line,)
    def update(i):
        phase = 2 * np.pi * (i / frames)
        line.set_ydata(np.sin(x - phase))
        return (line,)
    ani = FuncAnimation(
        fig,
        update,
        init_func=init,
        frames=frames,
        interval=1000 // fps,
        blit=True
    )
    if save:
        if save.endswith(".mp4"):
            ani.save(save, writer=FFMpegWriter(fps=fps, bitrate=2000), dpi=120)
        elif save.endswith(".gif"):
            from matplotlib.animation import PillowWriter
            ani.save(save, writer=PillowWriter(fps=fps), dpi=100)
    return ani