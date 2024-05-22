def funcion(): 
    while True:
        n=int(input("numeros entero\n--->"))
        lista=[]
        if n>0:
            for i in range(1,n+1):
                if i%3==0:
                    lista.append(i)
                elif i%5==0:
                    lista.append(i)
                elif i%7==0:
                    lista.append(i)
                
            
                
        else:
            print("numero invalido")
        
        x=sum(lista)
        print(x)
funcion()

