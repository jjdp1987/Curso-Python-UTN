# Un banco tiene 3 clientes que pueden hacer depósitos y extracciones. 
# También el banco requiere que al final del día calcule la cantidad de dinero que hay depositado.
# Lo primero que hacemos es identificar las clases:
# Podemos identificar la clase Cliente y la clase Banco.
# Luego debemos definir los atributos y los métodos de cada clase:

# EJERCICIO DE BANCO Y CLIENTES
# ----------------------------
# Cliente
#     atributos
#         nombre
#         monto
#     métodos
#         __init__
#         depositar
#         extraer
#         retornar_monto
#
# Banco
#     atributos
#         3 Cliente (3 objetos de la clase Cliente)
#     métodos
#         __init__
#         operar
#         depositos_totales

# Programa:

class Cliente:

    def __init__(self, nombre):
        self.nombre = nombre
        self.monto = 0

    def depositar(self, monto):
        self.monto = self.monto + monto

    def extraer(self, monto):
        self.monto = self.monto - monto

    def retornar_monto(self):
        return self.monto

    def imprimir(self):
        print(self.nombre, "tiene depositado la suma de", self.monto)


class Banco:
    
    def __init__(self):
        # Acá el Banco "contrata" a sus 3 clientes
        self.cliente1 = Cliente("Juan")
        self.cliente2 = Cliente("Ana")
        self.cliente3 = Cliente("Diego")

    def operar(self):
        # El banco manda órdenes a los objetos Cliente
        self.cliente1.depositar(100)
        self.cliente2.depositar(150)
        self.cliente3.depositar(200)
        self.cliente3.extraer(150)

    def depositos_totales(self):
        total = self.cliente1.retornar_monto() + self.cliente2.retornar_monto() + self.cliente3.retornar_monto()
        print("El total de dinero del banco es:", total)
        self.cliente1.imprimir()
        self.cliente2.imprimir()
        self.cliente3.imprimir()

# Bloque principal (donde arranca la magia)
banco1 = Banco()
banco1.operar()
banco1.depositos_totales()