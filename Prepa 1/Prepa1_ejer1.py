n1=str(input("Agregar el nombre del producto:"))
n2=float(input("Agregar el precio del producto:"))
n3=int(input("Agregar el numero de unidad del producto:"))
print("El producto escogido: {producto} , tiene un precio de :{precio:6.2f}, la cantidad de unidades es:{cantidad:3.0f} y  el monto total es :{total:8.2f}".format(producto=n1 , precio=n2, cantidad=n3, total=n2*n3 ))