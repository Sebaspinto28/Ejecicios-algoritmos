import random 
class Carrera:
    def __init__(self,id,caballos):
        self.id=id
        self.lista_caballos=caballos

    def inicio(self):
        print("Comineza")
        for caballo in self.lista_caballos:
            print(caballo.nombre)

    def ganador(self):
        ganador=random.choice()