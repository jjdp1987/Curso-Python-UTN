# Crear una clase Persona que tenga como atributo el nombre y la edad.
# El operador == retornará verdadero si las dos personas tienen la misma edad, el operador >
# retornará True si la edad del objeto de la izquierda tiene una edad mayor a la edad del objeto de la
# derecha del operador >, y así sucesivamente
# Programa:

class Persona:
    def __init__(self,nombre, edad):
        self.nombre=nombre
        self.edad=edad

    def __eq__(self,objeto2):
        if self.edad==objeto2.edad:
            return True
        else:
            return False

    def __ne__(self,objeto2):
        if self.edad!=objeto2.edad:
            return True
        else:
            return False

    def __gt__(self,objeto2):
        if self.edad>objeto2.edad:
            return True
        else:
            return False

    def __ge__(self,objeto2):
        if self.edad>=objeto2.edad:
            return True
        else:
            return False

    def __lt__(self,objeto2):
        if self.edad<objeto2.edad:
            return True
        else:
            return False

    def __le__(self,objeto2):
        if self.edad<=objeto2.edad:
            return True
        else:
            return False

# bloque principal

persona1=Persona('juan',22)
persona2=Persona('ana',22)
if persona1==persona2:
    print("Las dos personas tienen la misma edad.")
else:
    print("No tienen la misma edad.")