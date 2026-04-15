# Veamos con un ejemplo la sintaxis para redefinir el operador +.
# Crearemos una clase Cliente de un banco y redefiniremos el operador + para que nos retorne la
# suma de los depósitos de los dos clientes que estamos sumando.
# Programa:

class Cliente:

    def __init__(self,nombre,monto):
        self.nombre=nombre
        self.monto=monto

    def __add__(self,objeto2):
        s=self.monto+objeto2.monto
        return s

cli1=Cliente('Ana',1200)
cli2=Cliente('Luis',1500)
print("El total depositado por los dos clientes es")
print(cli1+cli2)