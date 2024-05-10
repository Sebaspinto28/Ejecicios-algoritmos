h=int(input("Agregar altura:"))
aux=1
auz=-1
for n1 in range(h):
    if aux ==1:
        print(aux)
    elif aux > 1:
        print( aux, end=" ")
        for n2 in range(1,0,-2):
            print(auz)
    aux+=2
    auz+=2
    
