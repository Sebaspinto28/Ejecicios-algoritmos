class Client:
    def __init__(self,id,name,age,number):
        self.id=id
        self.name=name
        self.age=age
        self.number=number
        
    def mostrar(self):
        return f"Cliente: {self.name} - Cedula: {self.id} - Edad: {self.age} - Telefono: {self.number}"