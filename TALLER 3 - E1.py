class Cuenta:
    def __init__(self, saldo, tasaAnual):
        self.saldo = saldo
        self.númeroConsignaciones = 0
        self.númeroRetiros = 0
        self.tasaAnual = tasaAnual
        self.comisiónMensual = 0.0

    def consignar(self, cantidad):
        self.saldo += cantidad
        self.númeroConsignaciones += 1

    def retirar(self, cantidad):
        nuevoSaldo = self.saldo - cantidad
        if nuevoSaldo >= 0:
            self.saldo -= cantidad
            self.númeroRetiros += 1
        else:
            print("La cantidad a retirar excede el saldo actual.")

    def calcularInterés(self):
        tasaMensual = self.tasaAnual / 12
        interesMensual = self.saldo * tasaMensual
        self.saldo += interesMensual

    def extractoMensual(self):
        self.saldo -= self.comisiónMensual
        self.calcularInterés()

class CuentaAhorros(Cuenta):
    def __init__(self, saldo, tasa):
        super().__init__(saldo, tasa)
        if saldo < 10000:
            self.activa = False
        else:
            self.activa = True

    def retirar(self, cantidad):
        if self.activa:
            super().retirar(cantidad)

    def consignar(self, cantidad):
        if self.activa:
            super().consignar(cantidad)

    def extractoMensual(self):
        if self.númeroRetiros > 4:
            self.comisiónMensual += (self.númeroRetiros - 4) * 1000
        super().extractoMensual()
        if self.saldo < 10000:
            self.activa = False

    def imprimir(self):
        print(f"Saldo = ${self.saldo}")
        print(f"Comisión mensual = ${self.comisiónMensual}")
        print(f"Número de transacciones = {self.númeroConsignaciones + self.númeroRetiros}")

class CuentaCorriente(Cuenta):
    def __init__(self, saldo, tasa):
        super().__init__(saldo, tasa)
        self.sobregiro = 0.0

    def retirar(self, cantidad):
        resultado = self.saldo - cantidad
        if resultado < 0:
            self.sobregiro -= resultado
            self.saldo = 0.0
        else:
            super().retirar(cantidad)

    def consignar(self, cantidad):
        residuo = self.sobregiro - cantidad
        if self.sobregiro > 0:
            if residuo > 0:
                self.sobregiro = 0.0
                self.saldo = residuo
            else:
                self.sobregiro = -residuo
                self.saldo = 0.0
        else:
            super().consignar(cantidad)

    def extractoMensual(self):
        super().extractoMensual()

    def imprimir(self):
        print(f"Saldo = ${self.saldo}")
        print(f"Cargo mensual = ${self.comisiónMensual}")
        print(f"Número de transacciones = {self.númeroConsignaciones + self.númeroRetiros}")
        print(f"Valor de sobregiro = ${self.sobregiro}")
        print()

class PruebaCuenta:
    @staticmethod
    def main():
        saldoInicialAhorros = float(input("Ingrese saldo inicial de la cuenta de ahorros: $"))
        tasaAhorros = float(input("Ingrese tasa de interés de la cuenta de ahorros: "))
        cuenta1 = CuentaAhorros(saldoInicialAhorros, tasaAhorros)
        cantidadDepositar = float(input("Ingrese cantidad a consignar en la cuenta de ahorros: $"))
        cuenta1.consignar(cantidadDepositar)
        cantidadRetirar = float(input("Ingrese cantidad a retirar de la cuenta de ahorros: $"))
        cuenta1.retirar(cantidadRetirar)
        cuenta1.extractoMensual()
        cuenta1.imprimir()

if __name__ == "__main__":
    PruebaCuenta.main()
    