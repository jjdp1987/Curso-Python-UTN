# Barras verticales

import matplotlib.pyplot as plt
categorias = ["A", "B", "C", "D"]
valores = [4, 7, 1, 8]
plt.bar(categorias, valores, color="red")
plt.title("Gráfico de barras")
plt.xlabel("Categorías")
plt.ylabel("Valores")
plt.show()

# Barras horizontales
import matplotlib.pyplot as plt
categorias = ["A", "B", "C", "D"]
valores = [4, 7, 1, 8]
plt.barh(categorias, valores, color="green")
plt.title("Gráfico de barras horizontal")
plt.xlabel("Valores")
plt.ylabel("Categorías")
plt.show()