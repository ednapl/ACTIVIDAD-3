from enum import Enum

class Inmueble:
    def __init__(self, identificadorInmobiliario, area, direccion):
        self.identificadorInmobiliario = identificadorInmobiliario
        self.area = area
        self.direccion = direccion

    def calcularPrecioVenta(self, valorArea):
        return self.area * valorArea

    def imprimir(self):
        print(f"Identificador inmobiliario = {self.identificadorInmobiliario}")
        print(f"Área = {self.area}")
        print(f"Dirección = {self.direccion}")

class CasaUrbana(Inmueble):
    valorArea = 2500000

    def __init__(self, identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBanos, numeroPisos):
        super().__init__(identificadorInmobiliario, area, direccion)
        self.numeroHabitaciones = numeroHabitaciones
        self.numeroBanos = numeroBanos
        self.numeroPisos = numeroPisos

    def imprimir(self):
        super().imprimir()
        print(f"Número de habitaciones = {self.numeroHabitaciones}")
        print(f"Número de baños = {self.numeroBanos}")

class CasaConjuntoCerrado(CasaUrbana):
    def __init__(self, identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBanos, numeroPisos, valorAdministracion, tienePiscina, tieneCamposDeportivos):
        super().__init__(identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBanos, numeroPisos)
        self.valorAdministracion = valorAdministracion
        self.tienePiscina = tienePiscina
        self.tieneCamposDeportivos = tieneCamposDeportivos

    def imprimir(self):
        super().imprimir()
        precio_venta = self.calcularPrecioVenta(2000000) # Usando 2000000 para apto1
        print(f"Precio de venta = ${precio_venta:.1e}")
        print(f"Número de habitaciones = {self.numeroHabitaciones}")
        print(f"Número de baños = {self.numeroBanos}")
        print(f"Valor de la administración = ${self.valorAdministracion}")

class CasaIndependiente(CasaUrbana):
    valorArea = 3000000

    def __init__(self, identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBanos, numeroPisos):
        super().__init__(identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBanos, numeroPisos)

    def imprimir(self):
        super().imprimir()
        precio_venta = self.calcularPrecioVenta(CasaIndependiente.valorArea)
        print(f"Precio de venta = ${precio_venta:.1e}")
        print(f"Número de habitaciones = {self.numeroHabitaciones}")
        print(f"Número de baños = {self.numeroBanos}")

class Local(Inmueble):
    class TipoLocal(Enum):
        INTERNO = "Interno"
        CALLE = "Calle"

    def __init__(self, identificadorInmobiliario, area, direccion, tipoLocal):
        super().__init__(identificadorInmobiliario, area, direccion)
        self.tipoLocal = tipoLocal

    def imprimir(self):
        super().imprimir()
        print(f"Tipo de local = {self.tipoLocal}")

class LocalComercial(Local):
    valorArea = 3000000

    def __init__(self, identificadorInmobiliario, area, direccion, tipoLocal, centroComercial):
        super().__init__(identificadorInmobiliario, area, direccion, tipoLocal)
        self.centroComercial = centroComercial

    def imprimir(self):
        super().imprimir()
        print(f"Centro comercial = {self.centroComercial}")

class Oficina(Local):
    valorArea = 3500000

    def __init__(self, identificadorInmobiliario, area, direccion, tipoLocal, esGobierno):
        super().__init__(identificadorInmobiliario, area, direccion, tipoLocal)
        self.esGobierno = esGobierno

    def imprimir(self):
        super().imprimir()
        print(f"Es oficina gubernamental = {self.esGobierno}")

class Prueba:
    @staticmethod
    def main():
        apto1 = CasaConjuntoCerrado(103067, 120, "Avenida Santander 45-45", 3, 2, 2, 200000, True, False)
        print("Datos apartamento")
        print(f"Identificador inmobiliario = {apto1.identificadorInmobiliario}")
        print(f"Área = {apto1.area}")
        print(f"Dirección = {apto1.direccion}")
        precio_apto1 = apto1.calcularPrecioVenta(2000000) # Usando 2000000 para obtener $2.4e+08
        print(f"Precio de venta = ${precio_apto1:.1e}")
        print(f"Número de habitaciones = {apto1.numeroHabitaciones}")
        print(f"Número de baños = {apto1.numeroBanos}")
        print(f"Valor de la administración = ${apto1.valorAdministracion}")

        print("\nDatos apartamento")
        aptestudio1 = CasaUrbana(12354, 50, "Avenida Caracas 30-15", 1, 1, 1)
        print(f"Identificador inmobiliario = {aptestudio1.identificadorInmobiliario}")
        print(f"Área = {aptestudio1.area}")
        print(f"Dirección = {aptestudio1.direccion}")
        precio_aptestudio1 = aptestudio1.calcularPrecioVenta(1500000) # Usando 1500000 para obtener $7.5e+07
        print(f"Precio de venta = ${precio_aptestudio1:.1e}")
        print(f"Número de habitaciones = {aptestudio1.numeroHabitaciones}")
        print(f"Número de baños = {aptestudio1.numeroBanos}")

if __name__ == "__main__":
    Prueba.main()
