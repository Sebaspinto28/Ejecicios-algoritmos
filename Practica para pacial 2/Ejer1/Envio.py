class Envio:
    def __init__(self,origen,destino,cliente,tracking,fecha,status,paquete):
        self.origen=origen
        self.destino=destino
        self.cliente=cliente
        self.tracking=tracking
        self.fecha=fecha
        self.status=status
        self.paquete=paquete
        

class Maritimo(Envio):
    
    def __init__(self, origen, destino, cliente, tracking, fecha, status, paquete):
        super().__init__(origen, destino, cliente, tracking, fecha, status, paquete)
        self.precio=5

    def costo(self):
        peso=(self.paquete.largo*self.paquete.alto*self.paquete.ancho*100)/5000
        costo=peso*self.precio
        return costo
    



class Aereo(Envio):
    def __init__(self, origen, destino, cliente, tracking, fecha, status, paquete):
        super().__init__(origen, destino, cliente, tracking, fecha, status, paquete)
        self.precio=6
    def costo(self):
        peso=self.paquete.peso
        costo=peso*self.precio
        return costo

