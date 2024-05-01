print("Welcome to pizzeria")
main_option=int(input("please enter your option\n1. vegetariano\n2. no vegetariano\n"))
if main_option == 1:
    print("Usted a escogido la pizza vegetariana")
    ingredientes=int(input("please enter your option\n1. pimiento\n2. tofu\n"))
    if ingredientes == 1:
        print("Usted a escogido la pizza con queso mazzarella, tomate y pimiento")
    elif ingredientes == 2:
        print("Usted a escogido la pizza con queso mazzarella, tomate y tofu")
    else :
        print("error")
elif main_option == 2:
    print("Usted a escogido la pizza no vegetariana")
    ingredientes=int(input("please enter your option\n1. peperoni\n2. jamon\n3.salmon\n"))
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
