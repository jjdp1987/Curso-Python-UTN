# Estilo pyplot (imperativo)
# Se basa en funciones globales
# como plt.plot() , plt.title() o plt.show() . Es rápido y muy cómodo
# para figuras sencillas.

import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [2, 4, 6])
plt.title("Estilo pyplot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# Estilo orientado a objetos (OO)
# Trabaja directamente con los objetos Figure y Axes . Brinda más flexibilidad y
# es ideal para composiciones complejas o con múltiples subplots.

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [2, 4, 6])
ax.set_title("Estilo orientado a objetos")
ax.set_xlabel("X")
ax.set_ylabel("Y")
plt.show()