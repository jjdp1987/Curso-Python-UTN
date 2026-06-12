# Los colores se pueden definir por nombre ( "red" ), abreviatura ( "r" ), código hexadecimal
# ( "#FF5733" ) o escala de grises ( "0.5" , donde 0 es negro y 1 blanco).
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]
plt.plot(x, y1, color="blue", label="Linea Azul")
plt.plot(x, y2, color="#FF5733", label="Linea Naranja")
plt.legend()
plt.show()

