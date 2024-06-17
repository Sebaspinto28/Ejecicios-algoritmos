from Product import Alimento
from Product import Bebida
from Product import Product

class App:
    
productos = [
{
'nombre': 'Manzanas',
'precio': 10,
'cantidad': 15,
'tipo': 'alimento',
'peso': '1 kg',
'fecha_caducidad': '2023-12-31'
},
{
'nombre': 'Agua Mineral',
'precio': 5,
'cantidad': 12,
'tipo': 'bebida',
'volumen': '500 ml',
'fecha_caducidad': '2023-10-31'
},
{
'nombre': 'Pan Integral',
'precio': 20,
'cantidad': 20,
'tipo': 'alimento',
'peso': '500 g',
'fecha_caducidad': '2023-11-30'
},
{
'nombre': 'Refresco de Cola',
'precio': 25,
'cantidad': 15,
'tipo': 'bebida',
'volumen': '1 l',
'fecha_caducidad': '2023-09-30'
},
{
'nombre': 'Arroz',
'precio': 20,
'cantidad': 25,
'tipo': 'alimento',
'peso': '1 kg',
'fecha_caducidad': '2024-02-28'
},
{
'nombre': 'Jugo de Naranja',
'precio': 22,
'cantidad': 12,
'tipo': 'bebida',
'volumen': '750 ml',
'fecha_caducidad': '2023-12-15'
},
{
'nombre': 'Pasta Integral',
'precio': 24,
'cantidad': 18,
'tipo': 'alimento',
'peso': '500 g',
'fecha_caducidad': '2023-11-15'
},
{
'nombre': 'Cerveza',
'precio': 20,
'cantidad': 24,
'tipo': 'bebida',
'volumen': '330 ml',
'fecha_caducidad': '2023-10-01'
},
{
'nombre': 'Huevos',
'precio': 10,
'cantidad': 30,
'tipo': 'alimento',
'peso': '1 docena',
'fecha_caducidad': '2023-12-10'
},
{
'nombre': 'Leche',
'precio': 12,
'cantidad': 15,
'tipo': 'bebida',
'volumen': '1 l',
'fecha_caducidad': '2023-11-10'
}
]
    
    
    def __init__(self,productos):
        self.productos = productos
        self.list_inventario=[]
    
        
    def regis_inventario(self,productos):
        for x in self.productos:
            for k,v in x.items():

                if k =='nombre':
                    nombre=v
                elif k =='precio':
                    precio=v
                elif k =='cantidad':
                    cantidad=v
                elif k =='tipo':
                    tipo=v
                elif k =='fecha_caducidad':
                    fecha=v
                elif k =='peso':
                    peso=v
                else:
                    volumen=v
            
            if tipo=='alimento':
                self.producto=Alimento(nombre,precio,cantidad,tipo,peso,fecha)
                self.list_inventario.append(self.producto)
            else:
                self.producto=Bebida(nombre,precio,cantidad,tipo,volumen,fecha)
                self.list_inventario.append(self.producto)

        return self.list_inventario
        #for product in self.productos:
        #    for index in product:
        #        nombre=index['nombre']
        #        precio=index['precio']
        #        cantidad=index['cantida']
        #        tipo=index['tipo']
        #        if tipo=='alimento':
        #            peso=index['peso']
        #            fecha=index['fecha_caducidad']
        #            new_p=Alimento(nombre,precio,cantidad,tipo,peso,fecha)
        #            self.list_inventario.append(new_p)
        #        else:
        #            volumen=index['volumen']
        #            fecha=index['fecha_caducidad']
        #            new_p=Bebida(nombre,precio,cantidad,tipo,volumen,fecha)
        #            self.list_inventario.append(new_p)
                
    
    def show_inventario(self):
        print(self.list_inventario)

        for k,v in enumerate(self.list_inventario):
            print(f'-----{k+1}-----')
            print(v.mostar())
                
                
    def regis_data(self):
        self.regis_inventario()
        self.show_inventario()

    def menu(self):
        self.regis_data()

        print('-- The tienda --\n Bienvenido/a')
        while True:
            print('''
1. Ver productos del inevtario
2. Ver Registrar un ciente
3. Realizar una compra
4. Imprimir factura
=========================
5. Salir
''')
            
            seleccion = input("Ingrese el número correspondiente a su selección:\n---> ")
            while not seleccion.isnumeric() or int(seleccion) not in range(1,6):
                print('Error')
                seleccion = input("Ingrese el número correspondiente a su selección:\n---> ")

            if seleccion == '1':
                print('\nVer productos del inevtario')
                self.show_inventario()
            elif seleccion == '2':
                print('\nRegistrar un ciente')
                self.show_inventario()
            elif seleccion == '3':
                print('\nRealizar una compra')
                self.show_inventario()
            elif seleccion == '4':
                print('\nImprimir factura')
                self.show_inventario()
            else:
                print('Gracias por su visita. Vuelva pronto...')
                break

