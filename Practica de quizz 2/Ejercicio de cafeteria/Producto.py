class Producto:
    def __init__(self,id,nombre,precio,cantidad):
        self.id = id
        self.nombre=nombre
        self.precio=precio
        self.cantidad=cantidad
    def show_attr(self):
        return f"ID: {self.id}\n Nombre: {self.nombre}\n Precio: {self.precio}\n Cantidad: {self.cantidad}"
    
class Postre(Producto):
    def __init__(self, id, nombre, precio, cantidad,es_vegano):
        super().__init__(id, nombre, precio, cantidad)
        self.es_vegano=es_vegano

    def show_attr(self):
        return super().show_attr()
    
    def ask_vegano(self):
        if (self.es_vegano):
            return "Si"
        else:
            return "No"
    
class Cafe(Producto):
    def __init__(self,id,nombre, precio, cantidad,tamano,es_descaifenado):
        super().__init__(id,nombre, precio, cantidad)
        self.tamano=tamano
        self.es_descaifenado=es_descaifenado
    def show_attr(self):
        return f"{super().show_attr()} \nTamaño: {self.tamano}\n Descaifenado: {self.es_descaifenado} "
    
    def ask_descaifenado(self):
        if (self.es_descaifenado): # Yo pienso que es asi , ella hace if (self.delivered):
            return "Si"
        else:
            return "No"
        

class Jugo(Producto):
    def __init__(self,id, nombre, precio, cantidad,sabor,contiene_azucar):
        super().__init__(id, nombre, precio, cantidad)
        self.sabor=sabor
        self.contiene_azucar=contiene_azucar
    def show_attr(self):
        return f"{super().show_attr()} \nSabor: {self.sabor}\n Azucar: {self.contiene_azucar} "
    
    def ask_azucar(self):
        if (self.contiene_azucar): # Yo pienso que es asi , ella hace if (self.delivered):
            return "Si"
        else:
            return "No"
        


    

    

