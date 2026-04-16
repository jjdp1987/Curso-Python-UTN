class Clase():
    def __init__(self, valor):
        self.valor = valor
    def __repr__(self):
        return f'{self.__class__.__name__}({repr(self.valor)})'
    
clase = Clase('uno')
str(clase) # "Clase('uno')"
repr(clase) # "Clase('uno')"