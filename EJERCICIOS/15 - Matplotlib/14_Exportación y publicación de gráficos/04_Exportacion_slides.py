import matplotlib as mpl
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 5.6), layout="constrained")
fig.savefig("slide.png", dpi=200, transparent=True)

# Utilizá figuras 16:9, fuentes grandes (14-18 pt) y líneas gruesas para proyectores.