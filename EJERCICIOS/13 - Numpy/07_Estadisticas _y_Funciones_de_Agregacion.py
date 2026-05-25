import numpy as np

# 7.1 Mínimo y máximo
# Con np.min() y np.max() obtenemos el valor más bajo y más alto de un array.

arr = np.array([5, 12, 7, 20, 15])
print("7.1 Mínimo:", np.min(arr)) # 5
print("7.1 Máximo:", np.max(arr)) # 20
# 👉 También existen los métodos .min() y .max() que funcionan igual:
print("7.1 Mínimo (método):", arr.min())
print("7.1 Máximo (método):", arr.max())


# 7.2 Media y mediana
# Media (promedio): np.mean() . Mediana (valor central): np.median() .

arr = np.array([1, 2, 3, 4, 5, 100])
print("7.2 Media:", np.mean(arr)) # 19.166...
print("7.2 Mediana:", np.median(arr)) # 3.5
# 👉 Diferencia clave: la media se ve afectada por valores extremos (outliers), mientras
# que la mediana no.


# 7.3 Desviación estándar
# La desviación estándar mide la dispersión de los datos respecto de la media.

arr = np.array([10, 12, 14, 16, 18])
print("7.3 Media:", np.mean(arr))
print("7.3 Desviación estándar:", np.std(arr)) # 2.828...


# 7.4 Suma y producto
# np.sum() suma todos los elementos; np.prod() multiplica todos los elementos.

arr = np.array([1, 2, 3, 4])
print("7.4 Suma:", np.sum(arr)) # 10
print("7.4 Producto:", np.prod(arr)) # 24


# 7.5 Operaciones a lo largo de ejes
# En matrices (2D) o arrays de más dimensiones, podemos aplicar funciones
# estadísticas por filas o columnas usando el parámetro axis .
# Regla: 
# axis=0 opera por columnas (a lo largo de las filas) 
# axis=1 opera por filas (a lo largo de las columnas).

mat = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print("7.5 Suma total:", np.sum(mat)) # 45
print("7.5 Suma por columnas:", np.sum(mat, axis=0)) # [12 15 18]
print("7.5 Suma por filas:", np.sum(mat, axis=1)) # [ 6 15 24]
print("7.5 Media por columnas:", np.mean(mat, axis=0)) # [4. 5. 6.]
print("7.5 Máximo por filas:", np.max(mat, axis=1)) # [3 6 9]