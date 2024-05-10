#tabla=(input("Escriba el numero de la tabla de multiplicar que desea ver\n--->"))
#
#while tabla.isnumeric():
#    tabla=int(tabla)
#    for n in range(1, 11):
#        print(f'{tabla} x {n} = {tabla * n}')
#    tabla=int(input("Escriba el numero de la tabla de multiplicar que desea ver\n--->"))
#print("bye")

tabla=int(input("Escriba el numero de la tabla de multiplicar que desea ver\n--->"))

while tabla:
    for n in range(1, 11):
        print(f'{tabla} x {n} = {tabla * n}')
    tabla=int(input("Escriba el numero de la tabla de multiplicar que desea ver\n--->"))
