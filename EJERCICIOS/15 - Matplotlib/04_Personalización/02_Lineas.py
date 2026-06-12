# Estilos de línea
# Algunos estilos frecuentes son "-" (sólido), "--" (punteado), "-." (guiones y puntos)
# y ":" (puntos).
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]
plt.plot(x, y1, linestyle="--", color="green", label="Linea punteada")
plt.plot(x, y2, linestyle=":", color="purple", label="Linea de puntos")
plt.legend()
plt.show()

