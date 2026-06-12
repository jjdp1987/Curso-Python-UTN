# Marcadores
# Los marcadores resaltan cada punto de la serie. Ejemplos
# habituales: "o" (círculo), "s" (cuadrado), "^" (triángulo) y "*" (estrella).
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]
plt.plot(x, y1, marker="o", color="red", label="Con circulos")
plt.plot(x, y2, marker="s", color="blue", label="Con cuadrados")
plt.legend()
plt.show()