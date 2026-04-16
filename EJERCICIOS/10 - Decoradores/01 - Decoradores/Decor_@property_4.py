# Queremos modelar un dispositivo con batería que tiene las siguientes reglas:
# La batería tiene un nivel de carga entre 0 y 100.
# No se puede asignar un valor fuera de ese rango (se lanza un error).
# Cada vez que se carga la batería, se actualiza el nivel.
# Cuando se descarga, el nivel no puede ser negativo.
# Se puede consultar el estado de la batería como porcentaje y también si está casi vacía (<20%).
# Usaremos @property para:
# Encapsular el atributo interno _nivel de la batería.
# Controlar la asignación de valores con validación.
# Crear una propiedad derivada casi_vacia que dependa del nivel.
# Programa:

class Bateria:
    def __init__(self):
        self._nivel = 100 # nivel inicial 100%

    @property
    def nivel(self):
        return self._nivel

    @nivel.setter
    def nivel(self, nuevo_valor):
        if nuevo_valor >= 0 and nuevo_valor <= 100:
            self._nivel = nuevo_valor
        else:
            raise ValueError("Error: el nivel de batería debe estar entre 0 y 100.")

    @property
    def casi_vacia(self):
        return self._nivel < 20

    def cargar(self, cantidad):
        print(f"Cargando {cantidad}%...")
        self.nivel = min(self._nivel + cantidad, 100)

    def descargar(self, cantidad):
        print(f"Descargando {cantidad}%...")
        self.nivel = max(self._nivel - cantidad, 0)

# Prueba

b = Bateria()
print("Nivel inicial:", b.nivel)
b.descargar(85)
print("Nivel después de descarga:", b.nivel)
print("¿Batería casi vacía?", b.casi_vacia)
b.cargar(50)
print("Nivel después de carga:", b.nivel)