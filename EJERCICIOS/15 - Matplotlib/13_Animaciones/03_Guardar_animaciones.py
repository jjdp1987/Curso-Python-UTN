# Para guardar, necesitás un writer disponible en tu entorno. Comprobálo con
# matplotlib.animation.writers.list().

# Guardar como GIF
from matplotlib.animation import PillowWriter
# ani = FuncAnimation(...)
writer = PillowWriter(fps=30)
ani.save("onda.gif", writer=writer, dpi=100)

# Guardar como MP4
from matplotlib.animation import FFMpegWriter
# ani = FuncAnimation(...)
writer = FFMpegWriter(fps=30, bitrate=1800)
ani.save("onda.mp4", writer=writer, dpi=120)


# Asegurate de tener FFmpeg instalado (PATH 💡 en Windows o gestor de paquetes en
# Linux/macOS).


