# Se emplean para mostrar la relación entre dos variables numéricas, detectando
# correlaciones o agrupamientos.
import matplotlib.pyplot as plt
# Datos
altura = [150, 160, 170, 180, 190, 200]
peso = [50, 60, 65, 80, 85, 95]
# Diagrama de dispersión
plt.scatter(altura, peso, color="red", marker="x")
plt.title("Relación entre altura y peso")
plt.xlabel("Altura (cm)")
plt.ylabel("Peso (kg)")
plt.show()