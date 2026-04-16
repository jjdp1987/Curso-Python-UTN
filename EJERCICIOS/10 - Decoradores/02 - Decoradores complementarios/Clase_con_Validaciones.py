class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self._saldo = saldo_inicial

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        self._saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        if cantidad > self._saldo:
            raise ValueError("Fondos insuficientes")
        self._saldo -= cantidad

cuenta = CuentaBancaria("Carlos", 1000)
print(f"Saldo: {cuenta.saldo}") # 1000
cuenta.depositar(500)
print(f"Saldo: {cuenta.saldo}") # 1500
cuenta.retirar(200)
print(f"Saldo: {cuenta.saldo}") # 1300