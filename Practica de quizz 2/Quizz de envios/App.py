from Person import Client
from Person import Worker
from DispatcherCompany import DispatcherCompany
from Package import Packages
class App:
    def __init__(self):
      self.clients=[]
      self.workers=[]
      self.dispatcher_companies=[]
      self.packages=[]
    
    #Opcion 1
    def show_workers(self):
        print("Empleados")
        for i,empleado in enumerate(self.workers):
            print(f"\n {i+1}. {empleado.show_attr()}")
    #Opcion 2 
    def show_dispatcher(self):
        print("Empresas de despacho")
        for i, despacho in enumerate(self.dispatcher_companies):
            print(f"\n {i+1}. {despacho.show_attr()}")
    #Opcion 3
    def confirm(self):
        print("Paquetes")
        for i, paquete in enumerate(self.packages):
            print(f"\n {i+1}. {paquete.show_attr()}")

        while True:
            try:
                id=int(input("Ingrse el ID del paquete que quiere confirmar\n--->"))
                exist=False
                for package in self.packages:
                    if id==package.id:
                        exist=True

                        if package.delivered:
                            print("El paquete ya ha sido entregado")
                        else:
                            package.delivered=True
                            print(f"Entrega confirmada \n {package.show_attr()}")

                        break
                if exist==False:
                    print("No existe el ID del paquete")
                    raise ValueError
                else:
                    break
            except:
                print("Dato invalido")

    def pen_clients(self):
        pen_packages=[]
        for package in self.packages:
            if package.delivered==False:
                pen_packages.append(package)

        clients=[]
        for client in self.clients:
            for package in pen_packages:
                if client.address == package.address:
                    clients.append(client)
                    break
        print("Clinetes con pedidos pendientes")
        for i, client in enumerate(clients):
            print(f"\n {i+1}. {client.show_attr()}")

    def registro(self,db):
        for objeto,lista in db.items():
            for datos in lista:
                if objeto=="clients":
                    cliente=Client(datos["id"], datos["name"], datos["address"])
                    self.clients.append(cliente)

                elif objeto=="workers":
                    empleado=Worker(datos["id"], datos["name"],datos["role"], datos["dispatches"])
                    self.workers.append(empleado)

                elif objeto=="dispatcher_companies":
                    compania=DispatcherCompany(datos["id"],datos["name"],datos["products"])
                    self.dispatcher_companies.append(compania)
                
                elif objeto=="packages":
                    paquete=Packages(datos["id"], datos["address"], datos["delivered"])
                    self.packages.append(paquete)

                    for dispatcher in self.dispatcher_companies:
                        for i, paquetes in enumerate(dispatcher.packages):
                            if paquetes==paquete.id:
                                dispatcher.packages[i]=paquete
                
    def start(self,db):
        self.registro(db)
        print("Bienvenido al despacho")
        while True:
            try:
                menu=input("\n Ingrese una de las opciones\n 1. Ver trabajdores\n 2. Ver compañias de despacho\n 3. Comfirmar entrega\n 4. Ver clientes con pedidos pendientes \n 5.Salir \n --->")
                if menu == "1":
                    self.show_workers()
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

        
