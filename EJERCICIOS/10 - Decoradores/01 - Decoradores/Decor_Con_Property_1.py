class Persona:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self._edad = edad

    @property
    def edad(self):
        """Getter para la edad"""
        return self._edad

    @edad.setter
    def edad(self, valor):
        """Setter para la edad"""
        if valor < 0:
                raise ValueError("La edad no puede ser negativa")
        self._edad = valor

    @edad.deleter
    def edad(self):
        """Deleter para la edad"""
        print("Eliminando edad...")
        del self._edad

# Uso
persona = Persona("Ana", 25)
print(persona.edad) # 25 - ¡Se usa como atributo!
persona.edad = 30 # ¡Se asigna como atributo!
print(persona.edad) # 30
# Esto daría error:
# persona.edad = -5 # ValueError: La edad no puede ser negativa