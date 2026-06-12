# Ajustar el rango de los ejes permite destacar una región específica de los datos o enfocar una
# zona de interés.

import matplotlib.pyplot as plt
x = [0, 1, 2, 3, 4, 5, 6]
y = [0, 1, 4, 9, 16, 25, 36]
plt.plot(x, y, marker="o")
plt.title("Ejemplo con limites de ejes")
plt.xlim(0, 6) # Limite para el eje X
plt.ylim(0, 40) # Limite para el eje Y
plt.show()


# También es posible invertir los ejes en los casos que lo requieran:

import matplotlib.pyplot as plt
x = [0, 1, 2, 3, 4, 5, 6]
y = [0, 1, 4, 9, 16, 25, 36]
plt.plot(x, y, marker="o")
plt.title("Limites invertidos")
plt.xlim(6, 0) # Invierte el eje X
plt.ylim(40, 0) # Invierte el eje Y
plt.show()