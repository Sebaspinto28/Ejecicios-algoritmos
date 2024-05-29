class Alumno:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

    def toString(self):
        return f"nombre: {self.nombre} , Edad: {self.edad}"