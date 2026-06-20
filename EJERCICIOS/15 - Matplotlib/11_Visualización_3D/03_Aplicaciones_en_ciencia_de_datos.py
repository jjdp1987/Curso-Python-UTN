# • Exploración de variables: cuando tenés tres atributos clave, un scatter 3D coloreado por
# clase permite inspeccionar separabilidad antes de entrenar un modelo.
# • Clustering: graficá las etiquetas de algoritmos como K-Means o DBSCAN para confirmar
# si los grupos están bien definidos o si existen solapamientos.
# • Regresión: compará la superficie predicha z = f(x, y) frente a los datos reales para detectar
# desviaciones o zonas mal ajustadas.
# • Reducción de dimensionalidad: al proyectar PCA/UMAP/t-SNE a tres dimensiones, el plot
# 3D ayuda a ubicar outliers y a entender la estructura global.
# • Datos geoespaciales: mallas de terreno, LiDAR o point clouds se benefician de superficies
# y sombreado para percibir relieve y densidad.
# • Sensores y series multivariadas: mapear (tiempo, variable1, variable2) como hélices u
# otras trayectorias evidencia ciclos, fases o anomalías.
# Buenas prácticas: ⚡ controlá la cámara con view_init, agregá colorbar cuando muestres
# magnitudes continuas y ajustá alpha o tamaños de marcador para evitar ruido visual.