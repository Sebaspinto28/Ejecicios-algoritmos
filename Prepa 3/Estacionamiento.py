from Vehiculo import Vehiculo

class Estacionamiento:
    def __init__(self):
        self.vehiculos=[]
    
    def registro(self):
        placa=input("placa")
        marca=input("marca")
        puesto=input("puesto")
        h_entrada=input("entrda")
        h_salida=input("salida")
        minus=input("minusvalido")
        vehiculo=Vehiculo(placa,marca, puesto, h_entrada,h_salida, minus)
        self.vehiculos.append(vehiculo)