print("Welcome to pizzeria")
main_option=int(input("opciones de pizza\n1. vegetariano\n2. no vegetariano\nescoja que tipo de pizza desea:"))
if main_option == 1:
    print("Usted a escogido la pizza vegetariana")
    ingredientes=int(input("Los ingredientes a escoger son:\n1. pimiento\n2. tofu\nescoja el que corresponda:"))
    if ingredientes == 1:
        print("Usted a escogido la pizza con queso mazzarella, tomate y pimiento")
    elif ingredientes == 2:
        print("Usted a escogido la pizza con queso mazzarella, tomate y tofu")
    else :
        print("error")
elif main_option == 2:
    print("Usted a escogido la pizza no vegetariana")
    ingredientes=int(input("Los ingredientes a escoger son:\n1. peperoni\n2. jamon\n3.salmon\nescoja el que corresponda:"))
    if ingredientes == 1:
        print("Usted a escogido la pizza con queso mazzarella, tomate y peperoni")
    elif ingredientes == 2:
        print("Usted a escogido la pizza con queso mazzarella, tomate y jamon")
    elif ingredientes == 3:
        print("Usted a escogido la pizza con queso mazzarella, tomate y salmon")
    else :
        print("error")
else :
    print("error")
