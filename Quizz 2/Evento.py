class Evento:
    def __init__(self,id,tipo,fecha,duracion,lugar,artista):
        self.id = id
        self.tipo = tipo
        self.fecha = fecha
        self.duracion = duracion
        self.lugar = lugar
        self.artistas = artista

    def agregar_artistas(self):
        self.artistas.append()
    def retirar_artista(self):
        pass

    def show_attr(self):
        return f"id: {self.id}\n tipo:{self.tipo}\nfecha: {self.fecha}\n duracion: {self.duracion}\n lugar:{self.lugar}\n artistas: {self.artistas}"