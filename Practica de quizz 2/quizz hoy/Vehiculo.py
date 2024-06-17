class Vehiculo:
    def __init__(self,id,tipo,ano,color,precio,disponible):
        self.id=id
        self.tipo=tipo
        self.ano=ano
        self.color=color
        self.precio=precio
        self.disponible=disponible
        self.veces_alquilado=0
    
    def mostar_detalle(self):
        return f"id:{self.id}\ntipo:{self.tipo}\nano:{self.ano}\ncolor:{self.color}\nprecio:{self.precio}\ndisponible:{self.disponible}\nveces alquilado:{self.veces_alquilado}"