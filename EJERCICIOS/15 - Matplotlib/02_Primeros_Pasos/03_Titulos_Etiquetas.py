import matplotlib.pyplot as plt
# Datos de ejemplo
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo"]
ventas = [500, 700, 800, 600, 900]
# Crear grafico
plt.plot(meses, ventas, marker="o", color="blue", linestyle="--")
# Configuracion basica
plt.title("Crecimiento de Ventas en el Primer Semestre")
plt.xlabel("Meses")
plt.ylabel("Ventas (USD)")
# Guardar y mostrar
plt.savefig("ventas.png", dpi=200)
plt.show()