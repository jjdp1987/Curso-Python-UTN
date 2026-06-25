from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import matplotlib.pyplot as plt
with PdfPages("reporte.pdf") as pdf:
    for i in range(1, 4):
        fig, ax = plt.subplots(figsize=(6, 4), layout="constrained")
        x = np.linspace(0, 2 * np.pi, 300)
        ax.plot(x, np.sin(i * x))
        ax.set_title(f"Página {i}")
        pdf.savefig(fig, bbox_inches="tight")
        plt.close(fig)