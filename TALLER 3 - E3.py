class Profesor:
    def imprimir(self):
        print("Es un profesor.")

class ProfesorTitular(Profesor):
    def imprimir(self):
        print("Es un profesor titular.")

class Prueba:
    @staticmethod
    def main():
        profesor1 = ProfesorTitular()
        profesor1.imprimir()

if __name__ == "__main__":
    Prueba.main()