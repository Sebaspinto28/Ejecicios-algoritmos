class Cliente:
    def __init__(self,nombre,dni,alquileres):
        self.nombre = nombre
        self.dni = dni
        self.alquileres = alquileres

    def devolver_vehiculo(self,vehiculo):
        self.alquileres.append(vehiculo)
        vehiculo.disponible=True

    
    def alquilar_vehiculo(self,vehiculo):
        self.alquileres.append(vehiculo)
        vehiculo.disponible=False

class ClientePersonal(Cliente):
    def __init__(self, nombre, dni,tipo):
        super().__init__(nombre, dni)
        self.tipo = "personal"

class Clientejuridico(Cliente):
    def __init__(self, nombre, dni):
        super().__init__(nombre, dni)
        self.tipo = "juridico"




    
        