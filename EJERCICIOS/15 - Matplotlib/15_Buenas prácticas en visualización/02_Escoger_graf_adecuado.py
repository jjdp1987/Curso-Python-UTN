import matplotlib.pyplot as plt
categorias = ["Producto A", "Producto B", "Producto C", "Producto D"]
valores = [120, 95, 180, 140]
orden = sorted(range(len(valores)), key=lambda i: valores[i])
cats_ord = [categorias[i] for i in orden]
vals_ord = [valores[i] for i in orden]
fig, ax = plt.subplots(layout="constrained")
ax.barh(cats_ord, vals_ord)
ax.set_title("Ventas por producto (ordenadas)")
ax.set_xlabel("Unidades")
plt.show()



