# Definir una clase Cliente que almacene un código de cliente y un nombre.
# En la clase Cliente definir una variable de clase de tipo lista que almacene todos los clientes que
# tienen suspendidas sus cuentas corrientes.
# Imprimir por pantalla todos los datos de clientes y el estado que se encuentra su cuenta corriente.

# Programa:

class Cliente:
    suspendidos=[]

    def __init__(self,codigo,nombre):
        self.codigo=codigo
        self.nombre=nombre

    def imprimir(self):
        print("Codigo:",self.codigo)
        print("Nombre:",self.nombre)
        self.esta_suspendido()

    def esta_suspendido(self):
        if self.codigo in Cliente.suspendidos:
            print("Esta suspendido")
        else:
            print("No esta suspendido")
            print("_____________________________")

    def suspender(self):
        Cliente.suspendidos.append(self.codigo)

# bloque principal

cliente1=Cliente(1,"Juan")
cliente2=Cliente(2,"Ana")
cliente3=Cliente(3,"Diego")
cliente4=Cliente(4,"Pedro")
cliente3.suspender()
cliente4.suspender()
cliente1.imprimir()
cliente2.imprimir()
cliente3.imprimir()
cliente4.imprimir()
print(Cliente.suspendidos)

# El programa define una clase Cliente con una variable de clase suspendidos que almacena los códigos de los clientes que tienen suspendidas sus cuentas corrientes. La clase tiene métodos para imprimir los datos del cliente, verificar si su cuenta está suspendida y suspender la cuenta. En el bloque principal, se crean varios clientes, se suspenden algunos de ellos y se imprimen sus datos y el estado de sus cuentas. Finalmente, se imprime la lista de clientes suspendidos.