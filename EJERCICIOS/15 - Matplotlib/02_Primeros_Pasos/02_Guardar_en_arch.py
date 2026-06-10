import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.title("Grafico simple de ejemplo")
# Guardar como imagen PNG
plt.savefig("grafico.png")
# Guardar con mayor resolucion (300 dpi)
plt.savefig("grafico_hd.png", dpi=300)
plt.show()