# Polimorfismo y Duck Typing en Python
# Python sigue el principio de duck typing, que se refiere a que, si un objeto «parece un pato» (es
# decir, tiene ciertos métodos o atributos) y «suena como un pato» (los métodos se comportan de
# cierta manera), entonces Python lo tratará como tal, sin preocuparse por la clase a la que pertenece.
# Ejemplo de Duck Typing

class Pato:
    def hacer_sonido(self):
        return "Cuac!"

class Persona:
    def hacer_sonido(self):
        return "Hola!"
    
def hacer_sonido_entidad(entidad):
        print(entidad.hacer_sonido())

# Uso de Duck Typing

pato = Pato()
persona = Persona()
hacer_sonido_entidad(pato) # Imprime "Cuac!"
hacer_sonido_entidad(persona) # Imprime "Hola!"