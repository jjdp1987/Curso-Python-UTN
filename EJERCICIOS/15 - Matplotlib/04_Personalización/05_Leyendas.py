# Leyendas ( legend )
# Las leyendas identifican cada serie del gráfico. Se define un label por serie y luego se llama
# a plt.legend() .

import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y1 = [1, 4, 9, 16]
y2 = [1, 2, 3, 4]
plt.plot(x, y1, label="Cuadrados")
plt.plot(x, y2, label="Lineal")
plt.legend(loc="upper left")
plt.title("Leyenda en la esquina superior izquierda")
plt.show()