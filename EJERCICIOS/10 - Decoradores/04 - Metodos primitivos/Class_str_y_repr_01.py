class Clase():
    def __init__(self, valor):
        self.valor = valor
    def __str__(self):
        return f'El valor es {self.valor}'

clase = Clase('uno')
str(clase) # 'El valor es 12'
repr(clase) # '<__main__.Clase object at 0x7fd903d33ad0>'