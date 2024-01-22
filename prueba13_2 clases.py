class objetos:
    pass

class animados(objetos):
    pass

class animales (animados):
    def comer(self):
        print ('comiendo')

    def mover(self):
        print ('moviendose')

    def respirar(self):
        print ('respirando')

class mamiferos (animales):
    def alimentan_crias_con_leche():
        print ('alimentando crias con leche')

class primates (mamiferos):
    def tiene_manos(self):
        pass

class humanos (primates):
    pass

class inanimados (objetos):
    pass

class edificios(inanimados):
    pass

class casas(edificios):
    pass

class reptiles (animales):
    def tienen_sangre_fria(self):
        pass

class tortugas (reptiles):
    def ponen_huevos(self):
        print ('poniendo huevos')
