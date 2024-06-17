class Product:
    def __init__(self, nombre, precio, cantidad,tipo):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.tipo = tipo
    def show(self):
        return f'''
Nombre : {self.nombre}
Precio: {self.precio}
cantidad: {self.cantidad}
Tipo: {self.tipo}
'''

class Alimento(Product):
    def __init__(self, nombre, precio, cantidad, tipo,peso,fecha):
        super().__init__(nombre, precio, cantidad, tipo)
        self.peso = peso
        self.fecha=fecha
        
    def show(self):
        return f'''{super().show()}
        Peso: {self.peso} gr
        Fecha de caducidad: {self.fecha}
        '''
            
    

class Bebida(Product):
    def __init__(self, nombre, precio, cantidad, tipo,volumen,fecha):
        super().__init__(nombre, precio, cantidad, tipo)
        self.volumen = volumen
        self.fecha=fecha

    def show(self):
        return f'''{super().show()}
        Volumen: {self.volumen} ml
        Fecha de caducidad: {self.fecha}
        '''
