# • Mantené la API orientada a objetos: definí fig, ax = plt.subplots() y pasá ax= a
# df.plot().
# • Usá nombres de columnas claros; se reutilizan como ejes y leyendas.
# • Para series temporales, aprovechá DatetimeIndex y formateo automático de ticks.
# • Prepará los datos con groupby, pivot, rolling o resample antes de graficar.
# • Evitá mezclar llamadas a plt.* sin ax cuando trabajás con varios subplots.
# • Usá .to_numpy() o np.asarray() para cálculos vectorizados pesados.