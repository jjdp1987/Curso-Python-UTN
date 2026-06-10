import matplotlib.pyplot as plt
# Crear figura y un eje
fig, ax = plt.subplots()
# Dibujar en el eje
ax.plot([1, 2, 3], [2, 4, 6])
# Titulos y etiquetas
ax.set_title("Ejemplo con Figure y Axes")
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
plt.show()