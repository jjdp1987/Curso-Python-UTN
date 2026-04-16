class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self._edad = edad # _ indica que es "privado"

    def get_edad(self):
        return self._edad

    def set_edad(self, valor):
        if valor < 0:
            raise ValueError("La edad no puede ser negativa")
        self._edad = valor

persona = Persona("Ana", 25)
print(persona.get_edad()) # 25
persona.set_edad(30)
print(persona.get_edad()) # 30