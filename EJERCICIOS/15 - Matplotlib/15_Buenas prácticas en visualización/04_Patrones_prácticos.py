import matplotlib.pyplot as plt
def layout_exportable(fig_path: str):
    fig, ax = plt.subplots(figsize=(6, 4), layout="constrained")
    # ... graficar ...
    fig.savefig(fig_path, dpi=300, bbox_inches="tight")
fig, ax = plt.subplots(figsize=(6, 4), layout="constrained")
ax.plot([1, 2, 3], [2, 4, 3], label="Serie A")
ax.annotate("Pico", xy=(2, 4), xytext=(2.5, 4.3),
            arrowprops={"arrowstyle": "->", "linewidth": 1})
ax.grid(True, linestyle="--", alpha=0.3)
ax.legend()
for x_val, y_val in zip([1, 2, 3], [2, 4, 3]):
    ax.text(x_val, y_val, f"{y_val:.1f}", va="bottom", ha="center", fontsize=9)
plt.show()