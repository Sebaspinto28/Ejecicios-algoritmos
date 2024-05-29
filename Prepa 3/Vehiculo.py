class Vehiculo:
    def __init__ (self,placa,marca, puesto, h_entrada,h_salida, minus):
        self.placa=placa
        self.marca=marca
        self.puesto=puesto
        self.h_entrada=h_entrada
        self.h_salida=h_salida
        self.minus=minus

    def toString(self):
        return f"marca: {self.marca}, placa: {self.marca}, puesto : {self.puesto}, hora de entrada: {self.h_entrada}, hora de salida: {self.h_salida}, minusvalidos: {self.minus}"