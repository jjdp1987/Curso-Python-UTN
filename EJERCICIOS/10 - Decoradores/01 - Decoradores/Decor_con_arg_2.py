# Creación una función que reciba como parámetro el nombre del jugador, luego tira dos dados y
# muestra el mensaje que gano si suma 7 y perdió en caso contrario. Crear una función decoradora
# que grabe en un archivo que se le pasa a la función decoradora el resultado de la tirada de los dos
# dados.
# Programa:

import random

def guardar_en_archivo(nombre_archivo):
    """Decorador que guarda la salida de la función en un archivo de texto con
jugador, dados y resultado."""
    def decorador(func):
        def envoltura(*args, **kwargs):
            dado1, dado2 = func(*args, **kwargs)
            total = dado1 + dado2
            if total == 7:
                resultado = "GANO"
            else:
                resultado = "PERDIO"
            with open(nombre_archivo, "a") as f:
                # Guardar nombre del jugador, valores de los dados y resultado
                f.write(f"{args[0]} {dado1} {dado2} {resultado}\n")
                print(f"{args[0]} {resultado} - Resultado guardado en {nombre_archivo}")
                return dado1, dado2, resultado
            return envoltura
        return decorador

# Función más interesante: lanzar dos dados @guardar_en_archivo("partidas.txt")

def jugar_dados(jugador):
    """Simula lanzar 2 dados y devuelve los valores de cada dado."""
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    print(f"{jugador} lanzó los dados: {dado1} + {dado2} = {dado1 + dado2}")
    return dado1, dado2

# Llamadas de ejemplo

jugar_dados("Diego")
jugar_dados("Carlos")
