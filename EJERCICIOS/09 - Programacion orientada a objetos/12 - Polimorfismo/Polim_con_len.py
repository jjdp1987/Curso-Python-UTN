# Polimorfismo con Módulos y Funciones Incorporadas
# Python tiene muchas funciones incorporadas y módulos que son polimórficos de manera implícita.
# Por ejemplo, la función len() es polimórfica porque puede calcular la longitud de diferentes tipos
# de objetos, como cadenas, listas o tuplas.
# Ejemplo de Polimorfismo con len()

print(len("Python")) # Funciona con cadenas (Imprime 6)
print(len([1, 2, 3, 4])) # Funciona con listas (Imprime 4)
print(len((10, 20, 30))) # Funciona con tuplas (Imprime 3)