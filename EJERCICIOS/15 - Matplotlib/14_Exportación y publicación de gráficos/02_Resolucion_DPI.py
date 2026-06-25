# • Web: 96-150 dpi.
# • Presentaciones: 150-200 dpi.
# • Publicaciones impresas: 300-600 dpi.
fig, ax = plt.subplots(figsize=(6, 4), layout="constrained")
fig.savefig("articulo.png", dpi=300)