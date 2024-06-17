class Artista:
    def __init__(self,nombre,biografia,tipo,tarifa_hora,evento):
        self.nombre = nombre
        self.biografia = biografia
        self.tipo = tipo
        self.tarifa_hora = tarifa_hora
        self.evento = evento

    def participar_evento(self):
        pass
    def abandonar_evento(self):
        pass

class Musico(Artista):
    def __init__(self,nombre,biografia,tipo,tarifa_hora,evento,instrumento):
        super().__init__(nombre,biografia,tipo,tarifa_hora,evento)
        self.instrumento = instrumento
class DJ(Artista):
    def __init__(self,nombre,biografia,tipo,tarifa_hora,evento,genero_musical):
        super().__init__(nombre,biografia,tipo,tarifa_hora,evento)
        self.genero_musical = genero_musical
class Comediante(Artista):
    def __init__(self,nombre,biografia,tipo,tarifa_hora,evento,especialidad):
        super().__init__(nombre,biografia,tipo,tarifa_hora,evento)
        self.especialidad = especialidad


        

        