class objetos:
    pass

class edificios(objetos):
    pass

class casas(edificios):
    pass


class animados(objetos):
    def animar(self):
        print ("estoy animado")

class animales(animados):
    def comer(self):
        print("comiendo")

    def andar(self):
        print("andando")

    def respirar(self):
        print("respirando")

class mamiferos(animales):
    def mamar(self):
        print("mamando")

class primates(mamiferos):
    def manosear(self):
        print("manoseando")

class humanos(primates):
    def chatear(self):
        print("estoy chateando")


class reptiles(animales):
    def reptar(self):
        print("reptando")

class tortugas(reptiles):
    def __init__(self, edad, altura, peso):
        self.edad = edad
        self.altura = altura
        self.peso = peso
        
    
    
    def tortugear(self):
        print("estoy tortugeando")

    def poner_huevos(self):
        print("poniendo huevos")

    def buscar(self):
        print("buscando")
        print("lo he encontrado")

    def buscar_comida(self):
        self.andar()
        self.buscar()
        self.comer()

    def reproducir(self):
        self.tortugear()
        self.buscar()
        self.poner_huevos()
        self.andar()

    def bailar(self):
        self.andar()
        self.andar()
        self.andar()
        









