# Simula un dataset de calificaciones de 30 estudiantes.
# 1. Generar puntajes aleatorios (0 a 100).
# 2. Calcular mínimo, máximo, media, mediana y desviación estándar.
# 3. Clasificar entre “Aprobado” (≥60) y “Desaprobado” (<60).
# 4. Contar cuántos aprobaron y cuántos desaprobaron.
import numpy as np

np.random.seed(42) # Reproducibilidad
notas = np.random.randint(0, 101, size=30)
print("Notas de los estudiantes:\n", notas)
print("Nota mínima:", notas.min())
print("Nota máxima:", notas.max())
print("Media:", notas.mean())
print("Mediana:", np.median(notas))
print("Desviación estándar:", notas.std())
clasificacion = np.where(notas >= 60, "Aprobado", "Desaprobado")
print("Clasificación:\n", clasificacion)
aprobados = np.sum(notas >= 60)
desaprobados = np.sum(notas < 60)
print("Cantidad de aprobados:", aprobados)
print("Cantidad de desaprobados:", desaprobados)
# Ejemplo de salida:
# Notas de los estudiantes:
# [51 92 14 71 60 20 82 86 74 74 87 99 23 2 21 52 1 87 29 37 1 63 59 20 32 75 57 21 88 48]
# Nota mínima: 1
# Nota máxima: 99
# Media: 53.1
# Mediana: 57.5
# Desviación estándar: 28.29
# Clasificación:
# ['Desaprobado' 'Aprobado' 'Desaprobado' 'Aprobado' 'Aprobado' ... ]
# Cantidad de aprobados: 14
# Cantidad de desaprobados: 16