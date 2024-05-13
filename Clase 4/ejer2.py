h=int(input("Agregar altura:"))
for i in range(1, h+1, 2):
    for j in range(i, 0, -2):
        print(j, end=' ')
    print('')
    
