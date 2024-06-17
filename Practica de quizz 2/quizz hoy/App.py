from Cliente import Cliente
from Vehiculo import Vehiculo
class App:
    def __init__(self):
        self.vehiculos=[]
        self.clientes=[]

    def registro(self,datos):
        for objeto,lista in datos.items():
            for dato in lista:
                if objeto=="vehiculos":
                    vehiculo=Vehiculo(id=dato["id"],tipo=dato["tipo"],ano=dato["año"],color=dato["color"],precio=dato["precio"],disponible=True)
                    self.vehiculos.append(vehiculo)
                
                elif objeto=="cliente":
                    cliente=Cliente(nombre=dato["nombre"],dni=dato["cedula"],tipo=dato["tipo"])
                    self.clientes.append(cliente)

    def show_carros(self):
        for vehiculo in self.vehiculos:
            print(vehiculo.mostar_detalle())

    def start(self,datos):
        self.registro(datos)
        print("Bienvenido al despacho")
        while True:
            try:
                menu=input("\n Ingrese una de las opciones\n 1. Ver carros\n 2. \n 3. \n 4.  \n 5.Salir \n --->")
                if menu == "1":
                    self.show_carros()
                elif menu == "2":
                    self.show_dispatcher()    
                elif menu=="3":
                    self.confirm()
                elif menu=="4":
                    self.pen_clients()
                elif menu=="5":
                    print("Hasta luego")
                    break
                else:
                    raise ValueError
            except:
                print('Dato invalido')