import numpy as np

# 9.1 Generación de números aleatorios ( np.random )
# Existen múltiples formas de generar números aleatorios:

# a) Un número aleatorio entre 0 y 1 ( random.rand )
print("9.1a Número aleatorio [0,1):", np.random.rand())

# b) Array de números aleatorios ( rand )
print("9.1b Array 1D:", np.random.rand(5)) # 5 números aleatorios
print("9.1b Matriz 2D:\n", np.random.rand(2, 3)) # Matriz 2x3

# c) Enteros aleatorios ( randint )
print("9.1c Enteros aleatorios:", np.random.randint(1, 10, size=5))
# 5 números entre 1 y 9


# 9.2 Distribuciones comunes
# NumPy permite simular distribuciones estadísticas.

# a) Distribución uniforme ( np.random.uniform )
# Genera valores entre un rango [a, b) con probabilidad uniforme.
arr = np.random.uniform(0, 10, size=5)
print("9.2a Distribución uniforme [0,10):", arr)

# b) Distribución normal o gaussiana ( np.random.normal )
# Muy utilizada en estadística y machine learning.
arr = np.random.normal(loc=0, scale=1, size=10)
print("9.2b Distribución normal (media=0, std=1):", arr)
# 👉 loc es la media; scale , la desviación estándar.

# c) Distribución binomial ( np.random.binomial )
# Se usa para experimentos “sí/no” (Bernoulli).
# Simulación: 10 experimentos, probabilidad de éxito 0.5, repetido 5 veces
arr = np.random.binomial(n=10, p=0.5, size=5)
print("9.2c Distribución binomial:", arr)
# 👉 Ejemplo típico: lanzar una moneda 10 veces y contar cuántas veces salió cara.


# 9.3 Fijar semillas ( np.random.seed )
# Sin semilla, cada ejecución produce valores distintos. Para reproducir resultados, fijamos una
# semilla.
np.random.seed(42)
print("9.3 Con semilla fija:", np.random.randint(1, 100, 5))
# Salida (repetible):
# Con semilla fija: [52 93 15 72 61]
# 👉 Es clave para experimentar y comparar modelos de forma justa.