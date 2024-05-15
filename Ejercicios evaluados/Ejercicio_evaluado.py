bola=int(input("color de la bolita que saco\n1.Blanco \n2.verde \n3.amarilla \n4.azul \n5.roja\nseleccione que color de la bola saco:"))
valor=float(input("Coloque el su cuenta a cancelar:"))
if bola==1:
    print(f"Usted no a obtenido ningun descuento su monto a pagar es de {valor}")
elif bola==2:
    print(f"Usted  a obtenido un descuento del 10% su monto a pagar es de {valor-(valor*0.1)}")
elif bola==3:
    print(f"Usted  a obtenido un descuento del 25% su monto a pagar es de {valor-(valor*0.25)}")
elif bola==4:
    print(f"Usted  a obtenido un descuento del 50% su monto a pagar es de {valor-(valor*0.50)}")
elif bola==5:
    print(f"Usted  a obtenido un descuento del 100% su monto a pagar es de {valor-(valor*1)}")
else:
    print("Error")