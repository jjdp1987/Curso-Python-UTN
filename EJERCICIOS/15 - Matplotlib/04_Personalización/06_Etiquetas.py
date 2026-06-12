# Etiquetas en los ejes
# Las etiquetas aportan contexto a los datos y facilitan la lectura del gráfico.
import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]
plt.plot(x, y)
plt.xlabel("Valores de X")
plt.ylabel("Valores de Y")
plt.title("Ejemplo con etiquetas en los ejes")
plt.show()