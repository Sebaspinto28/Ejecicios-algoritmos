class Materias:
    def __init__(self,name,credits):
        self.name=name
        self.credits=credits


class Pregrado(Materias):
    def __init__(self, name, credits,depa):
        super().__init__(name, credits)
        self.depa=depa


class Postgrado(Materias):
    def __init__(self, name, credits,diplo):
        super().__init__(name, credits)
        self.diplo=diplo