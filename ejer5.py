nivel= float(input("escriba su nivel meritorio:\n"))
paga=2400
if nivel==0.0:
    print(f"su nivel es inaceptable y su paga es de {paga*nivel} euros" )
elif nivel==0.4:
    print(f"su nivel es aceptable y su paga es de {paga*nivel} euros" )
elif nivel>=0.6:
    print(f"su nivel es meritorio y su paga es de {paga*nivel} euros" )
else:
    print("ERROR")