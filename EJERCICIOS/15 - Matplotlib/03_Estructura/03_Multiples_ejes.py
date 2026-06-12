import matplotlib.pyplot as plt
fig, (ax1, ax2) = plt.subplots(1, 2) # 1 fila, 2 columnas
# Primer grafico
ax1.plot([1, 2, 3], [1, 4, 9], color="red")
ax1.set_title("Grafico 1")
# Segundo grafico
ax2.plot([1, 2, 3], [1, 2, 3], color="blue")
ax2.set_title("Grafico 2")
plt.show()