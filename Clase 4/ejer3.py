tama=int(input("Escriba el numero del tama;o de su lista "))
lista=[]
lista1=[]
cosa=True
for i in range(tama):
    n=int(input("Agregue los numeros de su lista"))
    lista.append(n)
    lista1.append(n)
lista1.reverse()
for i in range(len(lista)):
    if lista[i]==lista1[i]:
        cosa=True
    else:
        cosa=False
        break
if cosa==True:
    print("capicua")
else:
    print("no")
