class App:
    def __init__(self):
        self.drinks=[]

    def start(self):
        print("\nBienvenido \n")

    while True:
        try:
            menu=int(input("ingrse la opcion que desea:\n1. registrar\n2.Ver\3.Comprar\n4.salir\n--->"))
            if menu ==1:
                self.regis_drink()
            elif menu==2:
                self.show_drink()
            elif menu==3:
                self.buy_drink()
            elif menu==4:
                break
            else:
                print("Escriba una opcion valida")


        except:
            print("Dato invalido")
