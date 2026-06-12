# Las anotaciones resaltan puntos específicos con texto y flechas que guían la atención.
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.plot(x, y, marker="o")
plt.title("Anotacion de un punto clave")
plt.annotate(
"Aqui esta 3",
xy=(3, 9),
xytext=(4, 15),
arrowprops=dict(facecolor="black", shrink=0.05)
)
plt.show()