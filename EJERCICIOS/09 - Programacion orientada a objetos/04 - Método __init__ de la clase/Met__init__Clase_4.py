# Implementar la clase Operaciones. Se deben cargar dos valores enteros por teclado en el
# método __init__, calcular su suma, resta, multiplicación y división, cada una en un método,
# imprimir dichos resultados. 

class Operaciones:
    def __init__(self):
        self.valor1=int(input("Ingrese primer valor:"))
        self.valor2=int(input("Ingrese segundo valor:"))

    def sumar(self):
        su=self.valor1+self.valor2
        print("La suma es",su)

    def restar(self):
        re=self.valor1-self.valor2
        print("La resta es",re)

    def multiplicar(self):
        pro=self.valor1*self.valor2
        print("El producto es",pro)

    def division(self):
        divi=self.valor1/self.valor2
        print("La division es",divi)

# bloque principal

operacion1=Operaciones()
operacion1.sumar()
operacion1.restar()
operacion1.multiplicar()
operacion1.division()