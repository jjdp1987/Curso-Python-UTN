import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 10.1 Uso de arrays de NumPy en Pandas
# Pandas se apoya en NumPy para manejar Series y DataFrames.

# a) Crear una Serie a partir de un array
arr = np.array([10, 20, 30, 40, 50])
serie = pd.Series(arr, index=["a", "b", "c", "d", "e"])
print("10.1 a)Serie de Pandas:\n", serie)
# Salida:
# Serie de Pandas:
# a 10
# b 20
# c 30
# d 40
# e 50
# dtype: int32

# b) Crear un DataFrame a partir de un array
mat = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
df = pd.DataFrame(mat, columns=["Col1", "Col2", "Col3"])
print("10.1 b)DataFrame de Pandas:\n", df)
# Salida:
# DataFrame de Pandas:
# Col1 Col2 Col3
# 0 1 2 3
# 1 4 5 6
# 2 7 8 9
# 👉 Gracias a NumPy, Pandas manipula grandes volúmenes de datos con
# eficiencia.


# 10.2 Uso de arrays de NumPy en Matplotlib
# Matplotlib utiliza arrays de NumPy para construir gráficos.

# a) Graficar una función matemática

# Generamos datos con NumPy
x = np.linspace(0, 10, 100)
y = np.sin(x)
# Gráfico
plt.plot(x, y, label="sin(x)", color="blue")
plt.title("Ejemplo con NumPy + Matplotlib")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
# 👉 Los arrays de NumPy permiten calcular los valores que luego se visualizan.

# b) Graficar datos aleatorios
np.random.seed(0)
data = np.random.normal(0, 1, 1000)
plt.hist(data, bins=30, color="orange", edgecolor="black")
plt.title("Histograma de distribución normal")
plt.show()
# 👉 NumPy genera los datos y Matplotlib los representa.


# 10.3 Conversión entre arrays y listas
# Es común convertir entre arrays de NumPy y listas nativas.

# a) De array a lista ( .tolist() )
arr = np.array([1, 2, 3, 4, 5])
lista = arr.tolist()
print("Array:", arr)
print("Convertido a lista:", lista)
# Salida:
# Array: [1 2 3 4 5]
# Convertido a lista: [1, 2, 3, 4, 5]

# b) De lista a array ( np.array )
lista = [10, 20, 30, 40]
arr = np.array(lista)
print("Lista:", lista)
print("Convertida a array:", arr)
# Salida:
# Lista: [10, 20, 30, 40]
# Convertida a array: [10 20 30 40]