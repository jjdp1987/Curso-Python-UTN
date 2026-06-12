import matplotlib.pyplot as plt
import numpy as np
# Generar datos aleatorios
datos = np.random.randn(1000) # Distribución normal
plt.hist(datos, bins=30, color="skyblue", edgecolor="blue")
plt.title("Histograma de distribución normal")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.show()