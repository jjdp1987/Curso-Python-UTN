# Imagina que estás creando un sistema de pago para una tienda en línea. Puedes tener diferentes
# métodos de pago como tarjeta de crédito, PayPal y criptomonedas, y cada uno tiene una forma
# distinta de procesar el pago.

# Ejemplo de Sistema de Pago con Polimorfismo

class Pago:
    def procesar_pago(self, cantidad):
        pass

class TarjetaCredito(Pago):
    def procesar_pago(self, cantidad):
        return f"Pago de {cantidad} realizado con Tarjeta de Crédito."

class PayPal(Pago):
    def procesar_pago(self, cantidad):
        return f"Pago de {cantidad} realizado con PayPal."

class Cripto(Pago):
    def procesar_pago(self, cantidad):
        return f"Pago de {cantidad} realizado con Criptomonedas."

# Función polimórfica para procesar cualquier tipo de pago
def realizar_pago(metodo_pago, cantidad):
    print(metodo_pago.procesar_pago(cantidad))

# Usar diferentes métodos de pago

tarjeta = TarjetaCredito()
paypal = PayPal()
cripto = Cripto()
realizar_pago(tarjeta, 100) # Imprime "Pago de 100 realizado con Tarjeta de Crédito."
realizar_pago(paypal, 150) # Imprime "Pago de 150 realizado con PayPal."
realizar_pago(cripto, 200) # Imprime "Pago de 200 realizado con Criptomonedas."