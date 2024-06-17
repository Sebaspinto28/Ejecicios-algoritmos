class   Cliente:
    def __init__(self,nombre,edad,cedula):
        self.nombre=nombre
        self.edad=edad
        self.cedula=cedula
    def show_attr(self):
        return f"\n Nombre: {self.nombre}\n Edad: {self.edad}\n Cedula: {self.cedula}"